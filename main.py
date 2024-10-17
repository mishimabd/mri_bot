from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ConversationHandler

from instructions import instructions
from mri import mri, handle_image_upload, in_development
from start import start_button

TELEGRAM_BOT_TOKEN = "8033239310:AAEbRjpLJdPfRGjlIwx390hRlvrF_mM-rDU"
WAITING_FOR_IMAGE = range(1)


def main():
    print(f"{datetime.now()} - Started")
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_button))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^(Анализ МРТ)$"), in_development))
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^(Как пользоваться ботом 📖)$"), instructions))
    application.add_handler(MessageHandler(filters.PHOTO, handle_image_upload))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
