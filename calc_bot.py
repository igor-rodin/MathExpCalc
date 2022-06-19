from telegram.ext import (
    Dispatcher, Updater, CommandHandler)
import cmd_handlers as chdl

BOT_TOKEN = "5411252859:AAGhcVNIvVDMmAQazSoZKdfrO3DodIdgZvU"


def init_handlers(dispather: Dispatcher):
    dispather.add_handler(CommandHandler(['start', 'help'], chdl.start))
    dispather.add_handler(CommandHandler('calc', chdl.calc))
    dispather.add_handler(CommandHandler('csum', chdl.csum))
    dispather.add_handler(CommandHandler('csub', chdl.csub))
    dispather.add_handler(CommandHandler('cmul', chdl.cmul))
    dispather.add_handler(CommandHandler('cdiv', chdl.cdiv))


def run():
    updater = Updater(token=BOT_TOKEN, use_context=True)
    print("Calcbot starterd work...")

    dp = updater.dispatcher
    init_handlers(dp)

    updater.start_polling(poll_interval=2, drop_pending_updates=True)
