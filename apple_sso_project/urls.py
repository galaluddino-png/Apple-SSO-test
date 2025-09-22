from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.shortcuts import render

def home_view(request):
    return JsonResponse({
        'message': 'Apple SSO Django Project',
        'endpoints': {
            'login': '/social-auth/login/apple-id/',
            'callback': '/social-auth/complete/apple-id/',
            'user_info': '/auth/user/',
            'logout': '/auth/logout/',
        }
    })

def test_view(request):
    return render(request, 'test.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('test/', test_view, name='test'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('auth/', include('authentication.urls')),
]