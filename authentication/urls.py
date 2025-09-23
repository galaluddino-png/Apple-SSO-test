from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.logout_view, name='logout'),
    path('login-error/', views.login_error, name='login_error'),
    path('welcome/', views.welcome_view, name='welcome'),
]