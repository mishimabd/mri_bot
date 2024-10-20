from telegram import Update


async def instructions(update: Update, context) -> None:
    instructions_message = (
        "Здравствуйте! Сейчас я вам расскажу как пользоваться ботом:\n\n"
        "<b>1. Запуск бота</b>\n"
        "   - Откройте Telegram и найдите вашего бота.\n"
        "   - Нажмите кнопку \"Старт\" или отправьте команду /start.\n\n"
        "<b>2. Главное меню</b>\n"
        "   - После запуска бота, вам будет предложено главное меню с кнопками:\n"
        "     - Анализ МРТ\n"
        "     - Как пользоваться ботом 📖\n\n"
        "<b>3. Анализ МРТ</b>\n"
        "   - Чтобы проанализировать МРТ снимок, просто отправьте фотографию снимка в чат.\n"
        "   - Бот использует модель машинного обучения для анализа изображения.\n"
        "   - В ответ вы получите вероятностные оценки возможных диагнозов в процентах.\n"
        "   - Пожалуйста, учтите, что результаты анализа носят рекомендательный характер и не заменяют консультацию врача.\n"
    )
    await update.message.reply_text(instructions_message, parse_mode="HTML")
