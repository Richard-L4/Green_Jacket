from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    # Main checkout page
    path('', views.checkout, name='checkout'),

    # Success page after a completed checkout
    path(
        'checkout_success/<order_number>/',
        views.checkout_success,
        name='checkout_success'
    ),

    # Webhook endpoint to handle Stripe events
    path('wh/', webhook, name='webhook'),

    # Caches checkout data before final submission
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),
]
