import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, StringRegexHandler, MessageHandler, filters

from asgiref.sync import sync_to_async

from vump_grpc_client.ext.utils import human_readable_bytes

from v2ray.models import Customer

logger = logging.getLogger(__name__)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="لطفا ایمیل خود را ارسال کنید.")


async def get_email_traffic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        customer: Customer = await (sync_to_async(Customer.objects.get)(email=update.message.text))
        text = 'میزان مصرف شما برابر است با:'
        text += f'\n{human_readable_bytes(customer.traffic)}'
        text += '\n\nآخرین زمان بروزرسانی ترافیک:'
        text += f'\n{customer.jalali_updated_at.strftime("%d %B %Y - %H:%M")}'
    except Customer.DoesNotExist:
        text = 'ایمیل شما ثبت نشده است.'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def main():
    from v2ray.models import VUMPConfiguration

    configuration = VUMPConfiguration.get_instance()
    application = ApplicationBuilder().token(configuration.tg_bot_token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Regex(r'^.*@vpn\d+.com$'), get_email_traffic))
    application.run_polling()
