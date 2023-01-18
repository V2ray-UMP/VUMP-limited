from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel


class Inbound(BaseModel):
    PROTOCOL_VMESS = 'vmess'
    PROTOCOL_CHOICES = (
        (PROTOCOL_VMESS, 'vmess'),
    )
    NETWORK_WS = 'ws'
    NETWORK_CHOICES = (
        (NETWORK_WS, 'ws'),
    )

    tag = models.CharField(_("Tag"), max_length=64, unique=True)
    host = models.CharField(_("Host"), max_length=64)
    port = models.IntegerField(_("Port"), unique=True)
    protocol = models.CharField(_("Protocol"), choices=PROTOCOL_CHOICES, default=PROTOCOL_VMESS, max_length=10)
    network = models.CharField(_('Network'), choices=NETWORK_CHOICES, default=NETWORK_WS, max_length=10)
    path = models.CharField(_('Path'), max_length=255, default='/')

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        verbose_name = _('Inbound')
        verbose_name_plural = _('Inbounds')
        unique_together = (
            ('host', 'port'),
        )
