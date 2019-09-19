from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')