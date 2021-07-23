from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser
# Register your models here.


class MyUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'last_login', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    # make the password in  a read only hash format
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(MyUser, MyUserAdmin)
