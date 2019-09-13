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

# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.helper = FormHelper()
#     self.helper.layout = Layout(
#         Row(
#             Column('title', css_class = 'form-group col-6'),
#             Column('location', css_class = 'form-group col-6')
#             )
#         )

# class UserForm(ModelForm):
#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'email'
#         ]