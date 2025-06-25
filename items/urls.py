from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='items'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/<int:pk>/image/', views.item_image, name='item_image'),

    path('item/<int:pk>/add_review/',
         views.add_review, name='add_review'),
    path('item/<int:pk>/edit_review/<int:review_id>/',
         views.edit_review, name='edit_review'),
    path('item/<int:pk>/delete_review/<int:review_id>/',
         views.delete_review, name='delete_review'),
    path('item/<int:item_id>/toggle_save/',
         views.toggle_save_item, name='toggle_save_item'),

    path('edit/<int:item_id>/',
         views.edit_item, name='edit_item'),
    path('delete/<int:pk>/',
         views.delete_item, name='delete_item'),
]
