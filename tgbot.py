import random
from telegram.ext import Updater, CommandHandler

# Список фильмов, которые можно рекомендовать
movies = [
    "Фильм 1",
    "Фильм 2",
    "Фильм 3",
    "Фильм 4",
    "Фильм 5",
]

# Функция для обработки команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я могу рекомендовать тебе фильм. Просто введи /recommend")

# Функция для обработки команды /recommend
def recommend(update, context):
    movie = random.choice(movies)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я рекомендую посмотреть фильм '{}'".format(movie))

# Создание экземпляра Updater и добавление обработчиков команд
def main():
    updater = Updater(token='', use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    recommend_handler = CommandHandler('recommend', recommend)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(recommend_handler)
    updater.start_polling()

if __name__ == '__main__':
    main()