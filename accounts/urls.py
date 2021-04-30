from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register', sign_up, name='register'),
    path('login', log_in, name='login'),
    path('token', token, name='token'),
    path('success', success, name='success'),
    path('verify/<auth_token>', verify, name='verify'),
    path('error', error_page, name='error'),
    
]