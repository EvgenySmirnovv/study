import telebot
from config import (TOKEN, keys)
from extensions import (ConvertionException, ValuesConverter)

bot = telebot.TeleBot(TOKEN)

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Привет, я бот по переводу валюты!"
                                      f"\n Напиши сначала через пробел:"
                                      f"\n <Имя валюты>"
                                      f"\n <Перевести валюту>"
                                      f"\n <Сумма валюты>"
                                      f"\n Так же чтобы узнать доступную валюту, введи /values")
    pass

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.title().split(" ")
        if len(values) != 3:
            raise ConvertionException("Слшком много параметров")

        quote, base, amout = values
        price = ValuesConverter.convert(quote, base, amout)
        result = float(amout) * float(price)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка пользователя. \n {e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = (f"За {amout} {quote} в {base} получается {result}"
                f"\nСтоимость {quote}: {price}")
        bot.send_message(message.chat.id, text)

# Обрабатываются аудиозаписи
@bot.message_handler(content_types=['audio'])
def handle_audio(message):
    bot.send_message(message.chat.id, "В данный момент не могу обрабатывать аудисообщения."
                                      "\n Приношу извинения за неудобство."
                                      "\n Введите запрос текстом.")
    pass
# Обрабатываем фото или картинку
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    bot.send_message(message.chat.id, f"Nice Mem =DD,  {message.chat.username}")
    pass

bot.polling()