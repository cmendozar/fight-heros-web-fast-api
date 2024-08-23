import os
import requests

KEY = os.environ.get('MAILGUN_KEY')
SANDBOX = os.environ.get('SANDBOX_MAILGUN')
SENDER = os.environ.get('SENDER_MAILGUN')
def send_mail(recipient, subject, text):
    request_url = f'https://api.mailgun.net/v3/{SANDBOX}/messages'

    request = requests.post(
        request_url,
        auth=('api', KEY),
        data={
            'from': SENDER,
            'to': recipient,
            'subject': subject,
            'text': text
        }
    )

    if request.status_code == 200:
        print('Correo electrónico enviado exitosamente.')
        print(request.json())
    else:
        print(request.status_code)
