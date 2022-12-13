import time
from multiprocessing.context import Process

import schedule
import telebot

from tokens import token

bot = telebot.TeleBot(token)


def send_message_16():
    bot.send_message('@letnya16k3', f'Коллеги, не забываем проставлять оценки смен кто до 16!\n'
                                    'Закрываем смену в DarkStore -> \nЗаходим в Самокат Про ->\n'
                                    'Нажимаем на ваши отработанные часы в сегодняшний день ->\n'
                                    'Оцениваем смену\n'
                                    'Спасибо за смену)')


def send_message_18():
    bot.send_message('@letnya16k3', f'Коллеги, не забываем проставлять оценки смен кто до 18!\n'
                                    'Закрываем смену в DarkStore -> \nЗаходим в Самокат Про ->\n'
                                    'Нажимаем на ваши отработанные часы в сегодняшний день ->\n'
                                    'Оцениваем смену\n'
                                    'Спасибо за смену)')


def send_message_20():
    bot.send_message('@letnya16k3', f'Коллеги, не забываем проставлять оценки смен кто до 20!\n'
                                    'Закрываем смену в DarkStore -> \nЗаходим в Самокат Про ->\n'
                                    'Нажимаем на ваши отработанные часы в сегодняшний день ->\n'
                                    'Оцениваем смену\n'
                                    'Спасибо за смену)')


def send_message_23():
    bot.send_message('@letnya16k3', f'Коллеги, не забываем проставлять оценки смен кто до 23!\n'
                                    'Закрываем смену в DarkStore -> \nЗаходим в Самокат Про ->\n'
                                    'Нажимаем на ваши отработанные часы в сегодняшний день ->\n'
                                    'Оцениваем смену\n'
                                    'Спасибо за смену)')


def send_message_00():
    bot.send_message('@letnya16k3', f'Коллеги, не забываем проставлять оценки смен!\n'
                                    'Закрываем смену в DarkStore -> \nЗаходим в Самокат Про ->\n'
                                    'Нажимаем на ваши отработанные часы в сегодняшний день ->\n'
                                    'Оцениваем смену\n'
                                    'Всем доброй ночи!)Спасибо за смену)')


def send_message_morning():
    bot.send_message('@letnya16k3', 'Всем доброе утро!\n'
                                    'Не опаздываем на смену, предупреждаем если по какой-либо причине опаздываете, '
                                    'написав в чат сюда!')


schedule.every().day.at("07:15:00").do(send_message_morning)
schedule.every().day.at("16:00:00").do(send_message_16)
schedule.every().day.at("18:00:00").do(send_message_18)
schedule.every().day.at("20:00:00").do(send_message_20)
schedule.every().day.at("23:00:00").do(send_message_23)
schedule.every().day.at("00:00:00").do(send_message_00)


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
        bot.send_message('@testbotchatlis', f'Коллеги, не забываем проставлять оценки смен!\n'
                                            'Закрываем смену в DarkStore -> \nЗаходим в Самокат Про ->\n'
                                            'Нажимаем на ваши отработанные часы в сегодняшний день ->\n'
                                            'Оцениваем смену\n'
                                            'Всем доброй ночи!)Спасибо за смену)')

    bot.polling()


if __name__ == '__main__':
    ScheduleMessage.start_process()
    try:
        telegram_bot(token)
    except:
        pass
