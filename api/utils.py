from django.core.mail import send_mail
from environs import Env
import requests

env = Env()
env.read_env()


def send_email(**kwargs):
    from_email = 'cehtarasivka2019@ukr.net'
    recipient_list = env.list('RECIVER_EMAIL')
    context = ""
    for item in kwargs:
        context += f"{item}: {kwargs[item]}\n"

    send_mail("Замовлення", context, from_email, recipient_list)


def send_mail_to_telegram(**kwargs):
    url = f"https://api.telegram.org/bot{env.str('TG_BOT_TOKEN')}/sendMessage"
    context = ""
    for item in kwargs:
        context += f"{item}: {kwargs[item]}\n"

    data = {'chat_id': env.int("RECIVER_TG_GROUP"), 'text': context}
    requests.post(url, json=data)
