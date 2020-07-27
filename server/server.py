import json

from flask import Flask, request

from weather.table_creator.api.api import API

app = Flask(__name__)


@app.route('/', methods=["POST"])
def send_request():
    api = API()
#   Сервер будет нужен, если программа научится делать что-то кроме создания файла,
#   Например, выдавать информацию в командную строку



if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
