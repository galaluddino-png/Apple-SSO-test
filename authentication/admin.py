from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'apple_user_id', 'created_at']
    search_fields = ['user__email', 'apple_user_id']