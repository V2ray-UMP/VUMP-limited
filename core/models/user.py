from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager

from . import BaseModel
from ..managers import BaseManager


class CustomUserManager(BaseUserManager, BaseManager):
    def create_user(self, username, password, is_staff=False, is_superuser=False, is_active=True, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")

        user_obj = self.model(
            username=username,
            **extra_fields,
        )
        user_obj.set_password(password)
        user_obj.is_staff = is_staff
        user_obj.is_superuser = is_superuser
        user_obj.is_active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields,
        )
        return user


class CustomUser(BaseModel, AbstractUser):
    objects = CustomUserManager()
    tg_id = models.PositiveBigIntegerField(_('TelegramID'), null=True, blank=True)

    @property
    def full_name(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
