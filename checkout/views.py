from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse
)
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import OrderForm
from .models import Order, OrderLineItem
from items.models import Item
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from trolley.contexts import trolley_contents

import stripe
import json
import logging

logger = logging.getLogger(__name__)


@require_POST
def cache_checkout_data(request):
    """
    Cache checkout data in Stripe PaymentIntent metadata.
    """
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                'trolley': json.dumps(request.session.get('trolley', {})),
                'save_info': request.POST.get('save_info'),
                'username': (
                    request.user.username
                    if request.user.is_authenticated else 'anonymous'
                ),
            }
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            'Sorry, your payment cannot be processed right now. '
            'Please try again later.'
        )
        logger.error(f"Stripe metadata update failed: {e}")
        return HttpResponse(content=str(e), status=400)


def checkout(request):
    """
    Process checkout: display form on GET, create order on POST.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        trolley = request.session.get('trolley', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_trolley = json.dumps(trolley)
            order.save()

            for item_id, item_data in trolley.items():
                try:
                    item = Item.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        OrderLineItem.objects.create(
                            order=order,
                            item=item,
                            quantity=item_data,
                        )
                    else:
                        for size, quantity in item_data[
                            'items_by_size'
                                ].items():

                            OrderLineItem.objects.create(
                                order=order,
                                item=item,
                                quantity=quantity,
                                item_size=size,
                            )
                except Item.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your trolley wasn't found "
                        "in our database. Please call us for assistance!"
                    )
                    logger.warning(
                        f"Item ID {item_id} not found. "
                        f"Order {order.order_number} deleted."
                    )
                    order.delete()
                    return redirect(reverse('view_trolley'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )
        else:
            messages.error(
                request,
                'There was an error with your form. '
                'Please double check your information.'
            )

    else:
        trolley = request.session.get('trolley', {})
        if not trolley:
            messages.error(
                request,
                "There's nothing in your trolley at the moment."
            )
            return redirect(reverse('items'))

        current_trolley = trolley_contents(request)
        total = current_trolley['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(
                request,
                'Stripe public key is missing. Did you forget to set it '
                'in your environment?'
            )

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkout: save user info if needed and send
    confirmation email.
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f'Order successfully processed! Your order number is {order_number}. '
        f'A confirmation email will be sent to {order.email}.'
    )

    # Render email templates
    subject = render_to_string(
        'checkout/confirmation_emails/confirmation_email_subject.txt',
        {'order': order}
    ).strip()

    body = render_to_string(
        'checkout/confirmation_emails/confirmation_email_body.txt',
        {
            'order': order,
            'contact_email': settings.DEFAULT_FROM_EMAIL,
        }
    )

    try:
        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            fail_silently=False,
        )
    except Exception as e:
        logger.error(f"Email send failed for order {order_number}: {e}")
        messages.warning(
            request,
            "Order placed, but confirmation email could not be sent."
        )

    if 'trolley' in request.session:
        del request.session['trolley']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
