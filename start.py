from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CallbackContext


async def start_button(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    buttons = [
        [KeyboardButton("Как пользоваться ботом 📖")],
        [KeyboardButton("Анализ МРТ")],
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    # Reply with a greeting message
    await update.message.reply_text(
        f"👋Добрый день, {user.first_name}! Я дипломная работа студента Astana IT University!",
        reply_markup=reply_markup, parse_mode="HTML"
    )