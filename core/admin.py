from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    # fieldsets = (
    #     (None, {'fields': ('e_mail', 'password')}),
    #     (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    #     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                    'groups', 'user_permissions')}),
    #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'first_name', 'last_name', 'e_mail', 'password1', 'password2'),
        }),
    )
    list_display = ('e_mail', 'first_name', 'last_name', 'is_staff')
    search_fields = ('e_mail', 'first_name', 'last_name')
    ordering = ('e_mail',)


admin.site.register(get_user_model(), CustomUserAdmin)
print('done'+str(get_user_model()))