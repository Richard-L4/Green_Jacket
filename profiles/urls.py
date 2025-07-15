from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the user profile page
    path('', views.profile, name='profile'),

    # URL pattern for viewing past order history by order number
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
    ),
]
