from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
class AccountAdmin(admin.StackedInline):
    list_display = ('username', 'phone', 'status')
    search_fields = ('username', 'status')
    model = Account
    can_delete = True
    verbose_name_plural = "account"

class UserAdmin(BaseUserAdmin):
    inlines = [AccountAdmin]
admin.site.unregister(User)
admin.site.register(User, UserAdmin)