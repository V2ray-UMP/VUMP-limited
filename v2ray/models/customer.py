from vump_grpc_client import VUMPClient

from asgiref.sync import async_to_sync

from telegram import Bot

import jdatetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

from ..models import VUMPConfiguration


class Customer(BaseModel):
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    download_traffic = models.PositiveIntegerField(
        verbose_name=_('Download Traffic'), default=0
    )
    upload_traffic = models.PositiveBigIntegerField(
        verbose_name=_('Upload Traffic'), default=0
    )
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)

    def reset_traffic(self):
        configuration = VUMPConfiguration.get_instance()
        vump_client = VUMPClient(
            host=configuration.server_ip, port=configuration.v2ray_api_port
        )
        vump_client.get_client_upload_traffic(email=self.email, reset=True)
        vump_client.get_client_download_traffic(email=self.email, reset=True)
        self.upload_traffic = self.download_traffic = 0
        Customer.objects.filter(pk=self.pk).update(upload_traffic=0, download_traffic=0)

    def update_traffics(self):
        configuration = VUMPConfiguration.get_instance()
        vump_client = VUMPClient(
            host=configuration.server_ip, port=configuration.v2ray_api_port
        )
        upload_traffic = vump_client.get_client_upload_traffic(
            email=self.email, reset=True
        )
        download_traffic = vump_client.get_client_download_traffic(
            email=self.email, reset=True
        )
        self.upload_traffic += upload_traffic
        self.download_traffic += download_traffic
        self.save()

    def check_traffic(self):
        configuration = VUMPConfiguration.get_instance()
        bot = Bot(configuration.tg_bot_token)
        if self.traffic >= configuration.max_traffic and self.is_active:
            async_to_sync(bot.send_message)(
                182714152, f'User {self.email} has used all traffic.'
            )
            self.save()
        elif self.traffic >= (configuration.max_traffic // 2) and self.is_active:
            async_to_sync(bot.send_message)(
                182714152, f'User {self.email} has used 50% of traffic.'
            )

    @property
    def jalali_updated_at(self):
        return jdatetime.datetime.fromgregorian(datetime=self.updated_at, locale='fa_IR')

    @property
    def traffic(self):
        return self.download_traffic + self.upload_traffic

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
