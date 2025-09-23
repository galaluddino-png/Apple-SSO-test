from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.user_info, name='user_info'),
    path('logout/', views.logout_view, name='logout'),
    path('login-success/', views.login_success, name='login_success'),
    path('login-error/', views.login_error, name='login_error'),
    path('welcome/', views.welcome_view, name='welcome'),
]