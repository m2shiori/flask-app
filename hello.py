# flaskからFlaskクラスをインポート
from flask import Flask

# Flaskクラスのインスタンスをつくって app 変数に入れる
app = Flask(__name__)

# /（ルート）にアクセスしたら次に書く関数(hello_world)を実行するという宣言
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
