from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .base import BaseAdmin


@admin.register(get_user_model())
class UserAdmin(BaseAdmin, BaseUserAdmin):
    list_display = (*BaseUserAdmin.list_display, 'tg_id')
    new_fields = ('tg_id',)

    def get_fieldsets(self, request, obj=None):
        old_fields = super(UserAdmin, self).get_fieldsets(request, obj)
        if obj:
            old_fields[1][1]['fields'] = tuple({*old_fields[1][1]['fields'], *self.new_fields})
        return old_fields
