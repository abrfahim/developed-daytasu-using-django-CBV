from django.urls import path
from . import views


# app distribution
app_name = 'auth_system'

urlpatterns = [
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
]