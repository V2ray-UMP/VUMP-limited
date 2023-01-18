from django.contrib import admin

from core.admin import BaseAdmin

from ..models import Customer


@admin.register(Customer)
class CustomerAdmin(BaseAdmin):
    fields = (
        'email',
        'download_traffic',
        'upload_traffic',
        'is_active',
    )
