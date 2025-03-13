from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен бота
TOKEN = "7572920994:AAEocmTP2otf2etxw0IV4PHbWJZSw95gU6E"

# URL твоего веб-приложения
WEB_APP_URL = "https://ваш-сайт.com"  # Замените на URL вашего веб-приложения

# Функция для обработки команды /start и отправки WebApp кнопки
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаем кнопку для WebApp
    keyboard = [
        [InlineKeyboardButton("Перейти в WebApp", web_app={"url": WEB_APP_URL})]
    ]
    
    # Создаем клавиатуру
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой для WebApp
    await update.message.reply_text('Привет! Нажми кнопку, чтобы открыть веб-приложение внутри Telegram:', reply_markup=reply_markup)

# Основная функция для запуска бота
def main() -> None:
    # Создание объекта Application и передача токена
    application = Application.builder().token(TOKEN).build()

    # Регистрация команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()





