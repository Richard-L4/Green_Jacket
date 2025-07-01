import json
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    trolley = request.session.get('trolley', {})
    
    if not trolley:
        messages.error(request, "There's nothing in your trolley at the moment")
        return redirect(reverse('items'))
    
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            # Save trolley data as JSON string in order
            order.original_trolley = json.dumps(trolley)
            order.save()
            # Here you would also create order line items etc.
            
            # Clear trolley after order is saved
            request.session['trolley'] = {}
            messages.success(request, 'Order successfully placed!')
            return redirect(reverse('order_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please check and try again.')
    else:
        order_form = OrderForm()
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)