from django.urls import path
from .views import *

urlpatterns = [
    path('register', UserRegistration.as_view(), name='register'),
    path('edit_login_settings', EditLoginSettings.as_view(), name='edit_login_settings'),
    path('password', ChangePassword.as_view(), name='password'),
    path('password_success', password_success, name='password_success'),
    path('<int:pk>/user_profile', UserProfile.as_view(), name='user_profile'),
    path('<int:pk>/edit_user_profile', EditUserProfile.as_view(), name='edit_user_profile'),
    path('create_user_profile', CreateUserProfile.as_view(), name='create_user_profile'),
]
