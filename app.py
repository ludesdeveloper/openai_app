import os
from flask import Flask
from flask import request
from flask import Response
import requests
from service_openai import get_response_openai

TOKEN = os.environ.get('TELEGRAMAPI')
app = Flask(__name__)


def parse_message(message):
    print("message-->", message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id, txt


def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }

    r = requests.post(url, json=payload)
    return r


@app.route('/telegram_open_ai', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        print(msg)
        check_userid = msg['message']['chat']['username']
        print(f'userid detected: {check_userid}')
        TELEGRAMUSERID = os.environ.get('TELEGRAMUSERID')
        if check_userid == TELEGRAMUSERID:
            chat_id, txt = parse_message(msg)
            openai_reply = get_response_openai(txt)
            for i in openai_reply:
                tel_send_message(chat_id, i['text'])

        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port='5000')
