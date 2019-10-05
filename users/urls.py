from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('editprofile/', views.EditProfile.as_view(), name = 'editprofile'),
    path('user_confirm_delete/<int:pk>', views.DeleteProfile.as_view(), name = 'user_confirm_delete')
]