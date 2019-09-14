from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Event, Category

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'location',
            'venue',
            'start_time',
            'end_time',
            'description',
            'categories'
        ]