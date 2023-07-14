from django.core.mail import send_mail
from environs import Env
import requests
from django.template import Template

env = Env()
env.read_env()

inputs_text = {
    "name": "Ім'я", "number": "Номер телефону",
    "message": "Коментарі до замовлення", "email": "Email",
    "address": "Адреса", "lname": "Прiзвище",

}


def send_email(data):
    from_email = env.str('SENDER_EMAIL')
    recipient_list = env.list('RECIVER_EMAIL')
    context = ""
    html_products = ""
    total = 0
    for item in data.keys():
        if item != "selectId":
            context += f"<b>{inputs_text[item]}</b>: {data[item]}<br>"

    if "selectId" in data.keys():
        for item in data['selectId']:
            total += (int(item['price']) * int(item['count']))
            html_products += f"""
            <br>
        <div style="display: flex;width:auto; height: 120px; gap: 20px;">
           <div style="flex: 1; margin-right: 30px;">
            <img style="object-fit: cover; object-position: center; width: 100%; height: 100%;" src="{item['images'][0]}" alt="">
            </div>
        <div style="flex: 1;">
            <h2 style="margin: 0;">{item['name']}</h2>
            <p style="margin: 0;">Знижка: <del style="color: red;">{item['discount']} <sup>грн</sup></del></p>
            <p style="margin: 0;">Ціна: <span style="color: limegreen;">{item['price']} <sup>грн</sup></span></p>
            <p style="margin: 0;">Кількість: <span style="color: chocolate;">{item['count']}</span></p>
        </div>
    </div>
            <br>
            """
    context += html_products
    context += f"<br><b>Всього:</b> {total}"
    send_mail(
        subject="Замовлення", message="Замовлення", html_message=context, from_email=from_email,
        recipient_list=recipient_list
    )


def send_mail_to_telegram(data):
    url = f"https://api.telegram.org/bot{env.str('TG_BOT_TOKEN')}/sendMessage"
    context = ""
    total = 0
    for item in data.keys():
        if item != "selectId":
            context += f"<b>{inputs_text[item]}</b>: {data[item]}\n"

    if "selectId" in data.keys():
        for item in data['selectId']:
            total += (int(item['price']) * int(item['count']))
            context += f"\n\n<b>{item['name']}</b>\n" \
                       f"Знижка: {item['discount']} грн\n" \
                       f"Ціна: {item['price']} грн\n" \
                       f"Кількість: {item['count']}\n"

        context += f"<b>Всього</b>: {total}"

    data_items = {'chat_id': env.int("RECIVER_TG_GROUP"), 'text': context, 'parse_mode': 'html'}
    requests.post(url, json=data_items)
