from celery import shared_task

from telegram import Bot

from asgiref.sync import async_to_sync

from .models import Customer, VUMPConfiguration


@shared_task(name='check_all_users_traffic')
def check_all_users_traffic():
    configuration = VUMPConfiguration.get_instance()
    bot = Bot(configuration.tg_bot_token)
    async_to_sync(bot.send_message)(182714152, f'Starting check traffic.')
    for customer in Customer.objects.all():
        customer: Customer
        customer.update_traffics()
        customer.check_traffic()
