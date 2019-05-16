from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='loginapp'),
    path('register/', views.user_register, name='registration'),
]
