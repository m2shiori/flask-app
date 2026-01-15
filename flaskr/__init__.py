from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base

Base = declarative_base()
db = SQLAlchemy()  # SQLAlchemyのインスタンス作成

def create_app():
    app = Flask(__name__)
    # データベースファイルの保存先を指定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskr.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # blueprintの登録
    from . import blogs
    app.register_blueprint(blogs.blog_bp)

    # データベースのテーブルを自動作成
    with app.app_context():
        db.create_all()

    return app