# Generated by Django 4.1.3 on 2023-01-18 17:28

import django.core.validators
from django.db import migrations, models
import uuid
import v2ray.models.vump_configuration


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Email"
                    ),
                ),
                (
                    "download_traffic",
                    models.PositiveIntegerField(
                        default=0, verbose_name="Download Traffic"
                    ),
                ),
                (
                    "upload_traffic",
                    models.PositiveBigIntegerField(
                        default=0, verbose_name="Upload Traffic"
                    ),
                ),
                ("is_active", models.BooleanField(default=True, verbose_name="Active")),
            ],
            options={
                "verbose_name": "Customer",
                "verbose_name_plural": "Customers",
            },
        ),
        migrations.CreateModel(
            name="VUMPConfiguration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "server_ip",
                    models.GenericIPAddressField(verbose_name="Server IP address"),
                ),
                (
                    "v2ray_api_port",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(limit_value=65535)
                        ],
                        verbose_name="API port",
                    ),
                ),
                (
                    "v2ray_config_file_path",
                    models.FilePathField(
                        match=".*\\.json$",
                        path=v2ray.models.vump_configuration.default_file_path,
                        recursive=True,
                        verbose_name="Configuration file path",
                    ),
                ),
                (
                    "max_traffic",
                    models.PositiveIntegerField(verbose_name="Max Traffic"),
                ),
                (
                    "tg_bot_token",
                    models.CharField(
                        blank=True,
                        max_length=46,
                        null=True,
                        verbose_name="TG Bot Token",
                    ),
                ),
            ],
            options={
                "verbose_name": "VUMP Configuration",
                "verbose_name_plural": "VUMP Configuration",
                "unique_together": {("server_ip", "v2ray_api_port")},
            },
        ),
        migrations.CreateModel(
            name="Inbound",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, unique=True, verbose_name="UUID"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "tag",
                    models.CharField(max_length=64, unique=True, verbose_name="Tag"),
                ),
                ("host", models.CharField(max_length=64, verbose_name="Host")),
                ("port", models.IntegerField(unique=True, verbose_name="Port")),
                (
                    "protocol",
                    models.CharField(
                        choices=[("vmess", "vmess")],
                        default="vmess",
                        max_length=10,
                        verbose_name="Protocol",
                    ),
                ),
                (
                    "network",
                    models.CharField(
                        choices=[("ws", "ws")],
                        default="ws",
                        max_length=10,
                        verbose_name="Network",
                    ),
                ),
                (
                    "path",
                    models.CharField(default="/", max_length=255, verbose_name="Path"),
                ),
            ],
            options={
                "verbose_name": "Inbound",
                "verbose_name_plural": "Inbounds",
                "unique_together": {("host", "port")},
            },
        ),
    ]
