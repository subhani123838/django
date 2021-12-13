from django.apps import AppConfig
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed

class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapp'

    def ready(self):
        import blogapp.signals

