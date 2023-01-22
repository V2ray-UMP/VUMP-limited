from pathlib import Path

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _

from core.models import SingletonModel


def default_file_path():
    path = Path(settings.BASE_DIR / 'config' / 'v2ray')
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


class VUMPConfiguration(SingletonModel):
    server_ip = models.GenericIPAddressField(verbose_name=_('Server IP address'))
    v2ray_api_port = models.PositiveIntegerField(
        verbose_name=_('API port'),
        validators=[MaxValueValidator(limit_value=65535)],
    )
    v2ray_config_file_path = models.FilePathField(
        verbose_name=_('Configuration file path'),
        path=default_file_path,
        recursive=True,
        match='.*\.json$',
        allow_files=True,
        allow_folders=False,
    )
    max_traffic = models.PositiveIntegerField(verbose_name=_('Max Traffic'))
    tg_bot_token = models.CharField(
        verbose_name=_('TG Bot Token'),
        max_length=46,
        null=True, blank=True,
    )

    @classmethod
    def get_instance(cls) -> 'VUMPConfiguration':
        return super().get_instance()

    def __str__(self):
        return f'Click to edit configuration'

    class Meta:
        verbose_name = _('VUMP Configuration')
        verbose_name_plural = _('VUMP Configuration')
        unique_together = (
            ('server_ip', 'v2ray_api_port'),
        )
