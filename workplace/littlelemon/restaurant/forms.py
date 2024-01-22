from django.forms import ModelForm
from .models import Booking


class BookingForm(ModelForm):
    """
    A form for creating or updating a booking.

    Inherits from ModelForm and uses the Booking model.
    """
    class Meta:
        model = Booking
        fields = "__all__"
