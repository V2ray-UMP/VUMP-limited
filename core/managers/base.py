from django.db import models
from django.db.models.manager import BaseManager


class BaseQuerySet(models.query.QuerySet):
    pass


class CustomBaseManager(BaseManager.from_queryset(BaseQuerySet)):
    pass
