from django.contrib import admin
from django.contrib.auth import admin as u_admin
from accounts.models import User, Account
# Register your models here.

admin.site.register(Account)

class UserAdmin(u_admin.UserAdmin):
    list_display = ['first_name', 'last_name', 'email', 'is_superuser']

    
admin.site.register(User, UserAdmin)
