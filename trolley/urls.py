from django.urls import path
from . import views

urlpatterns = [
    # View the trolley contents
    path(
        '',
        views.view_trolley,
        name='view_trolley',
    ),

    # Add an item to the trolley
    path(
        'add/<item_id>/',
        views.add_to_trolley,
        name='add_to_trolley',
    ),

    # Adjust the quantity of a specific item in the trolley
    path(
        'adjust/<item_id>/',
        views.adjust_trolley,
        name='adjust_trolley',
    ),

    # Remove an item from the trolley
    path(
        'remove/<item_id>/',
        views.remove_from_trolley,
        name='remove_from_trolley',
    ),
]
