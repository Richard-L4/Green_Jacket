from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    Configuration for the Profiles app.
    Sets the default auto field type and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
