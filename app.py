from datetime import datetime
from flask import Flask, request
import pytz
import random

# Flaskのインスタンスをappという名前で作成
app = Flask(__name__)


# localhost:5000にアクセスした時の処理
@app.route('/', methods=['GET'])
def raretech_message():
    return '夢は、目標に向かって毎日歩みを進めた者だけが叶えられる。\
            今日の二時間は、その一歩だ'


# /timeへgetでアクセスしたら現在時刻を知らせる
@app.route('/time', methods=['GET'])
def current_time():
    dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
    date = dt_now.strftime('%Y年%m月%d日  %H時%M分%S秒')
    return f'現在時刻は{date}です'


# /dateにアクセスすると、入力メッセージが表示される
@app.route('/date', methods=['POST'])
def week_caluculation():
    """
    コマンド例: curl -X POST -d 'days=2022-10-03' http://localhost:5000/date
    """

    w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    input_date = request.form.get('days')
    # 受け取った文字を日付に変換する
    date = datetime.strptime(input_date, '%Y-%m-%d')

    # 日付を曜日に変換する
    week = date.weekday()

    return f'{date}は{w_list[week]}です'


# /aphorismへアクセスすると、名言をランダムに返す
@app.route('/aphorism', methods=['GET'])
def aphorism():
    aphorism_words = ['じゅんし久しぶり', 'あかんやん', 'aa', 'iii',]

    aphorism = random.choice(aphorism_words)

    return aphorism


@app.route('/fortune', methods=['GET'])
def random_fortune():
    fortunes = ['大吉', '中吉', '小吉', '吉']

    fortune = random.choice(fortunes)

    if fortune == '大吉':
        return f'おめ'
    else:
        return f'ドンマイ'


if __name__ == "main":
    app.run(debug=True)
