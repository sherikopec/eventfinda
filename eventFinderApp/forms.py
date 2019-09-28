from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Event, Category
from django import forms

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'

class EventForm(ModelForm):
    class Meta:
        model = Event
        exclude = ['host']
        widgets = {
            'start_time': DateTimeInput(),
            'end_time': DateTimeInput()
        }