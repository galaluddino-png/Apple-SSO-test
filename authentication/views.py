from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json


def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'})

def login_error(request):
    return JsonResponse({
        'status': 'error',
        'message': 'Login failed',
        'error': request.GET.get('message', 'Unknown error')
    }, status=400)

@login_required
def welcome_view(request):
    user = request.user
    full_name = f"{user.first_name} {user.last_name}".strip()
    if not full_name:
        full_name = user.username

    context = {
        'user': user,
        'full_name': full_name,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }
    return render(request, 'authentication/welcome.html', context)