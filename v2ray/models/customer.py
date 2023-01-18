from vump_grpc_client import VUMPClient

from django.db import models, utils
from django.utils.translation import gettext_lazy as _

from core.models import BaseModel

from ..models import VUMPConfiguration

try:
    configuration = VUMPConfiguration.get_instance()
except (utils.IntegrityError, utils.OperationalError):
    pass


class Customer(BaseModel):
    email = models.EmailField(verbose_name=_('Email'), unique=True)
    download_traffic = models.PositiveIntegerField(verbose_name=_('Download Traffic'), default=0)
    upload_traffic = models.PositiveBigIntegerField(verbose_name=_('Upload Traffic'), default=0)
    is_active = models.BooleanField(verbose_name=_('Active'), default=True)

    def reset_traffic(self):
        vump_client = VUMPClient(host=configuration.server_ip, port=configuration.v2ray_api_port)
        vump_client.get_client_upload_traffic(email=self.email, reset=True)
        vump_client.get_client_download_traffic(email=self.email, reset=True)
        self.upload_traffic = self.download_traffic = 0
        Customer.objects.filter(pk=self.pk).update(upload_traffic=0, download_traffic=0)

    def update_traffics(self):
        vump_client = VUMPClient(host=configuration.server_ip, port=configuration.v2ray_api_port)
        upload_traffic = vump_client.get_client_upload_traffic(email=self.email, reset=True)
        download_traffic = vump_client.get_client_download_traffic(email=self.email, reset=True)
        self.upload_traffic += upload_traffic
        self.download_traffic += download_traffic
        self.save(update_fields=('upload_traffic', 'download_traffic'))

    @property
    def traffic(self):
        return self.download_traffic + self.upload_traffic

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')
