from django.contrib import admin
from .models import User, OtpCode
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)
admin.site.register(User)


class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'expire_time')


admin.site.register(OtpCode, OtpCodeAdmin)

# class UserAdmin(BaseUserAdmin):
#     list_display = ('email', 'phone_number', 'is_admin')
#     list_filter = ('is_admin',)
# admin.site.register(User, UserAdmin)
