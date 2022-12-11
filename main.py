import time
from multiprocessing.context import Process

import schedule
import telebot

from tokens import token

bot = telebot.TeleBot(token)


def send_message1():
    bot.send_message('@testbotchatlis', 'Коллеги, не забываем проставлять оценки смен!'
                                        'Закрываем смену в DarkStore -> заходим в Самокат Про -> '
                                        '-> Нажимаем на ваши часы в сегодняшний день ->'
                                        'Оцениваем смену')


schedule.every().day.at("16:00:00").do(send_message1)
schedule.every().day.at("19:10:00").do(send_message1)
schedule.every().day.at("23:00:00").do(send_message1)
schedule.every().day.at("00:00:00").do(send_message1)


class ScheduleMessage():
    def try_send_schedule():
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_process():
        p1 = Process(target=ScheduleMessage.try_send_schedule, args=())
        p1.start()


def telegram_bot(token):
    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, 'Здаров битконисsт')

    bot.polling()


if __name__ == '__main__':
    ScheduleMessage.start_process()
    try:
        telegram_bot(token)
    except:
        pass
