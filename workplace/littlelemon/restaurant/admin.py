from django.contrib import admin
from .models import Booking
from .models import Menu


def admin_register_models():
    """
    Register the Menu and Booking models with the Django admin site.
    """
    admin.site.register(Menu)
    admin.site.register(Booking)

admin_register_models()
