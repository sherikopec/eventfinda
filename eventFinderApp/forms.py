from django.forms import ModelForm
from .models import Event, Category, User

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'location',
            'venue',
            'start_time',
            'end_time',
            'categories'
        ]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email'
        ]