from django.contrib import admin

from import_export.admin import ImportExportMixin
from djangoql.admin import DjangoQLSearchMixin


class BaseAdmin(DjangoQLSearchMixin, ImportExportMixin, admin.ModelAdmin):
    class Media:
        pass
