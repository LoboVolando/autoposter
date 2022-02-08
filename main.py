import os

import telebot
import logica


api_key = config('MY_TOKEN')
my_bot = telebot.TeleBot(api_key)
answers = {'привет': 'Как дела?'}

manual = '/help - инфрмация по командам бота\n' \
         '/lowprice - поиск отелей с <b>минимальной ценой</b>\n' \
         '/highprice - поиск отелей с <b>максимальной ценой</b>\n' \
         '/bestdeal - <b>лучшие предложения</b> в заданном диапазоне цен и расстоянии от центра\n'


@my_bot.message_handler(commands=['/start'])
def send_to_start(message: telebot.types.Message) -> None:
    """
    Отвечает 'Добрый день' на команду /start и отправляет список команд.
    :param message: Any передается команда /start.
    :return: None
    """

    my_bot.reply_to(message, f'Добрый день, {message.chat.first_name}')
    # bot.send_message(message.chat.id, manual, parse_mode="HTML")
    # logica.karamba(1, message.chat.)


@my_bot.message_handler(content_types=['photo'])
def send_to_photo(message: telebot.types.Message) -> None:
    """
    Отвечает 'Добрый день' на команду /start и отправляет список команд.
    :param message: Any передается команда /start.
    :return: None
    """
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
    """
    Функция ответа на текстовые сообщения пользователя. В процессе диалога в функуиях lowprice, highprice или
    bestdeal отвечает текстовыми сообщениями или кнопками выбора. Вне диалога на сообщения из ключей словаря answers
    отвечает соответствующими значениями вне зависимости от регистра ключа. На остальные сообщения предлагает поиск
    отелей и отправляет список команд
    отвечает 'Как дела?'
    :param message: Any передается текстовое сообщение
    :return: None
    """

    my_bot.reply_to(message, f'{message.chat.first_name}, got your message')
    text = message.text
    if text != 'Post':
        response = logica.karamba(1, text)
    else:
        response = logica.karamba(3, text)
    my_bot.reply_to(message, response)

#
# @logger.catch
# @bot.callback_query_handler(func=lambda call: True)
# def handle_text(call: telebot.types.CallbackQuery) -> None:
#     """
#     Функция ответа на CallbackQuery - результаты нажатия кнопок пользователем. В процессе диалога в функуиях
#     lowprice, highprice или bestdeal отвечает CallbackQuery пользователем. Вне диалога сообщает о неактуальности,
#     предлагает сделать новый поиск и отправляет список команд.
#     :param call: Any передается CallbackQuery
#     :return: None
#     """
#
#     try:
#         if sessions_redis.get_users(call.from_user.id, 'command'):
#             if call.data.isalpha():
#                 send_text = call.data
#             else:
#                 send_text = 'Вы выбрали локацию'
#
#             bot.edit_message_text(chat_id=call.message.chat.id,
#                                   message_id=call.message.id,
#                                   text=send_text)
#
#             if sessions_redis.get_users(call.from_user.id, 'command') == 'best':
#                 reply = bestdeal.handler(call.from_user.id, call.data)
#             else:
#                 reply = low_high_price.handler(call.from_user.id, call.data)
#
#             for index in range(len(reply)):
#                 bot.send_message(call.from_user.id, reply[index], parse_mode="HTML")
#         else:
#             bot.send_message(call.from_user.id, "Неактуально. Начните новый поиск", parse_mode="HTML")
#             bot.send_message(call.from_user.id, manual, parse_mode="HTML")
#
#     except (ValueError, IndexError, TypeError, KeyError, AttributeError, ConnectionError, NameError, Exception) as er:
#         bot.send_message(call.from_user.id, 'Произошла фатальная ошибка')
#         bot.send_message(call.from_user.id, 'Попробуйте новый поиск отелей. Вот команды:')
#         bot.send_message(call.from_user.id, manual, parse_mode="HTML")
#
#         sessions_redis.remove(call.from_user.id)
#         logger.exception(er)
#         pass


if __name__ == '__main__':
    my_bot.polling(none_stop=True, interval=20)
