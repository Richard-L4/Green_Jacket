"""items/urls.py

URL patterns for item-related views, including listing items, viewing
item details, saving items, and managing reviews.
"""

from django.urls import path
from . import views

urlpatterns = [
    # View all items
    path('', views.all_items, name='items'),

    # View item detail and image separately
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/<int:pk>/image/', views.item_image, name='item_image'),

    # Review CRUD for individual items
    path('item/<int:pk>/add_review/', views.add_review, name='add_review'),
    path(
        'item/<int:pk>/edit_review/<int:review_id>/',
        views.edit_review,
        name='edit_review'
    ),
    path(
        'item/<int:pk>/delete_review/<int:review_id>/',
        views.delete_review,
        name='delete_review'
    ),

    # Toggle saving an item (like a "save for later" feature)
    path(
        'item/<int:item_id>/toggle_save/',
        views.toggle_save_item,
        name='toggle_save_item'
    ),

    # Admin: Add, edit, and delete items
    path('add/', views.add_item, name='add_item'),
    path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
]
