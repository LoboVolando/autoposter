import os

import telebot
import logica


api_key = config('MY_TOKEN')
my_bot = telebot.TeleBot(api_key)


@my_bot.message_handler(content_types=['photo'])
def send_to_photo(message: telebot.types.Message) -> None:
  
    new_file = my_bot.get_file(message.photo[-1].file_id)

    downloaded_file = my_bot.download_file(new_file.file_path)
    src = new_file.file_path
    print(src)

    with open(src, 'wb') as file:
        file.write(downloaded_file)

    my_bot.reply_to(message, f'{message.chat.first_name}, got your file')
    response = logica.karamba(2, src)
    my_bot.reply_to(message, response)


@my_bot.message_handler(func=lambda message: True)
def handle_text(message: telebot.types.Message) -> None:
    
    my_bot.reply_to(message, f'{message.chat.first_name}, got your message')
    text = message.text
    if text != 'Post':
        response = logica.karamba(1, text)
    else:
        response = logica.karamba(3, text)
    my_bot.reply_to(message, response)

         
if __name__ == '__main__':
    my_bot.polling(none_stop=True, interval=20)
