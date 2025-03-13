from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен, который ты получил от BotFather
TOKEN = "7572920994:AAEocmTP2otf2etxw0IV4PHbWJZSw95gU6E"

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я твой Telegram-бот.')

# Основная функция
def main() -> None:
    # Создание Application и передача токена
    application = Application.builder().token(TOKEN).build()

    # Регистрация обработчика для команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()














from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен бота
TOKEN = "7572920994:AAEocmTP2otf2etxw0IV4PHbWJZSw95gU6E"

# Функция для обработки команды /start и отображения клавиатуры
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаём кнопки
    keyboard = [['Привет', 'Пока']]
    
    # Создаём клавиатуру на основе кнопок
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    # Отправляем сообщение с клавиатурой
    await update.message.reply_text('Выбери опцию:', reply_markup=reply_markup)

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















from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токен бота
TOKEN = "7572920994:AAEocmTP2otf2etxw0IV4PHbWJZSw95gU6E"

# Функция для обработки команды /start и отображения клавиатуры
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаём кнопки
    keyboard = [['Привет', 'Пока']]
    
    # Создаём клавиатуру на основе кнопок
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    # Отправляем сообщение с клавиатурой
    await update.message.reply_text('Выбери опцию:', reply_markup=reply_markup)

# Функция для обработки нажатия кнопок
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    
    if text == 'Привет':
        await update.message.reply_text('Привет! Как дела?')
    elif text == 'Пока':
        await update.message.reply_text('До свидания!')

# Основная функция для запуска бота
def main() -> None:
    # Создание объекта Application и передача токена
    application = Application.builder().token(TOKEN).build()

    # Регистрация команды /start
    application.add_handler(CommandHandler("start", start))

    # Регистрация обработчика для текста сообщений (кнопки)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()











from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токен бота
TOKEN = "7572920994:AAEocmTP2otf2etxw0IV4PHbWJZSw95gU6E"

# Функция для обработки команды /start и отображения клавиатуры
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаём кнопки
    keyboard = [['Нажми меня']]
    
    # Создаём клавиатуру на основе кнопок
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)

    # Отправляем сообщение с клавиатурой
    await update.message.reply_text('Добро пожаловать в мини-приложение! Нажми на кнопку:', reply_markup=reply_markup)

# Функция для обработки нажатия кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    
    if text == 'Нажми меня':
        await update.message.reply_text('Ты нажал на кнопку! Приложение работает!')

# Основная функция для запуска бота
def main() -> None:
    # Создание объекта Application и передача токена
    application = Application.builder().token(TOKEN).build()

    # Регистрация команды /start
    application.add_handler(CommandHandler("start", start))

    # Регистрация обработчика для текста сообщений (кнопки)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, button_handler))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()


