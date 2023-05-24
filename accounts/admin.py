from django.contrib import admin
from .models import User, OtpCode
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserCreationForm, UserChangeForm


class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'expire_time')


admin.site.register(OtpCode, OtpCodeAdmin)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('personal information', {'fields': ('email', 'full_name', 'phone_number', 'image', 'password', 'last_login')}),
        ('university information', {'fields': ('university', 'is_qut_student', 'student_number')}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        ('personal information', {'fields': ('email', 'full_name', 'phone_number', 'image', 'password1', 'password2')}),
        ('university information', {'fields': ('is_qut_student', 'student_number')}),
        ('permissions', {'fields': ('is_active', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}),

    )

    search_fields = ('email',)
    ordering = ('full_name',)
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, UserAdmin)
