from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def user_info(request):
    user = request.user
    return JsonResponse({
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'is_authenticated': user.is_authenticated,
    })

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})

def login_success(request):
    user = request.user
    return JsonResponse({
        'status': 'success',
        'message': 'Login successful',
        'user': {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        } if user.is_authenticated else None
    })

def login_error(request):
    return JsonResponse({
        'status': 'error',
        'message': 'Login failed',
        'error': request.GET.get('message', 'Unknown error')
    }, status=400)