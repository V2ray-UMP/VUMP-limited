from django.contrib import admin

from djangoql.admin import DjangoQLSearchMixin


class BaseAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    class Media:
        pass
