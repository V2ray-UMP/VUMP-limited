from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Run telegram bot in polling mode"
    can_import_settings = True

    def handle(self, *args, **options):
        from django_telegrambot import telegrambot
        telegrambot.main()

