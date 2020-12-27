from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('email', )
    search_fields = ('email', )
    ordering = ('email', )
    readonly_fields = (
        'last_login', 'date_joined'
    )

admin.site.register(User, CustomUserAdmin)
