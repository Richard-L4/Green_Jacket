"""
green_jacket URL Configuration

"""

from django.contrib import admin
from django.urls import path, include
from clubhouse import views

# For serving static files in development
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('clubhouse.urls')),
    path('items/', include('items.urls')),
    path('who-we-are/', views.who_we_are, name='who_we_are'),
    path('trolley/', include('trolley.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
]

# Serve static files during development only (when DEBUG=True)
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
