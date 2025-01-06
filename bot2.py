from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен твоего бота, который ты получаешь через BotFather
TOKEN = "7231177760:AAFZGjJvma8Mc0NSf96nLa076PjyzfoQWeM"

# Функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Кнопка, которая открывает WebApp внутри Telegram
    button = KeyboardButton("Open Store", web_app={"url": "https://all-parts.vercel.app/"})
    markup = ReplyKeyboardMarkup([[button]], resize_keyboard=True)

    # Отправляем приветственное сообщение с кнопкой
    await update.message.reply_text(
        "Welcome! Click the button below to open the AllParts Store.",
        reply_markup=markup,
    )

# Главная функция для запуска бота
def main() -> None:
    # Создаем объект Application с токеном бота
    application = Application.builder().token(TOKEN).build()

    # Добавляем команду /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()
