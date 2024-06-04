from twilio.rest import Client
from Z_pega_satus import info
import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1twOeHF9HuJv6wdwnPt0kXk6lqQdrtp8YGsFDxhXHm9Q')
worksheet = sh.sheet1


def send_message(phone, text):
    account_sid = 'AC6aec3786dc595e2aaa2657a0e4168aa2'
    auth_token = 'e1b7935d888ed2af8c10ebc763450cd1'

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=text,
        to=f'whatsapp:{phone}'
    )

    print(message.sid)
    print(f'SMS ENVIADO PARA {phone}')


def send_status():
    clientes = worksheet.get_all_records()
    for cliente in clientes:
        number = f'+{cliente["Phone"]}'
        phone = number
        print(phone)
        code = cliente['Code']
        text=info(code)
        send_message(phone,text)
        print(
            f'Mensagem enviada para o número:{phone}, referente ao pedido {code}')


