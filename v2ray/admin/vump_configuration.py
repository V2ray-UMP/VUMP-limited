from django.contrib import admin

from core.admin import BaseAdmin

from ..models import VUMPConfiguration


@admin.register(VUMPConfiguration)
class VUMPConfigurationAdmin(BaseAdmin):
    fields = (
        'server_ip',
        'v2ray_api_port',
        'v2ray_config_file_path',
        'max_traffic',
        'tg_bot_token',
    )

    def has_delete_permission(self, request, obj=None):
        return False
