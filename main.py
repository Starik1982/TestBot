from flask import Flask
from flask_sslify import SSLify
from flask import request
from flask import jsonify
import misc
import requests
import json
app = Flask(__name__)
ssllify = SSLify(app)

URL = 'https://api.telegram.org/bot' + misc.token


def write_json(date, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(date, f, indent=2, ensure_ascii=False)


def send_message(chat_id, text='Hello!'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


# def get_update():
#     url = URL + 'getUpdates'
#     r = requests.get(url)
#     #
#     return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']
        if 'hello' in message:
            send_message(chat_id, text='Hello Дорогуша :)')
        #write_json(r)
        return jsonify(r)
    return "<H1>Test Bot</H1>"


# def main():
#     r = get_update()
#     chat_id = r['result'][-1]['message']['chat']['id']
#     send_message(chat_id)
#     pass


if __name__ == '__main__':
    app.run()



