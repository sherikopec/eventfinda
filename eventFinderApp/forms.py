from django.forms import ModelForm, SplitDateTimeField
from crispy_forms.helper import FormHelper
from .models import Event, Category
from django import forms
from django.contrib.admin import widgets

# class DateTimeInput(forms.DateTimeInput):
#     input_type = 'date'

class EventForm(ModelForm):
    start_time = SplitDateTimeField(widget = widgets.AdminSplitDateTime())
    end_time = SplitDateTimeField(widget = widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        exclude = ['host']