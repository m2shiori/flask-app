from flaskr import create_app, db
from flaskr.models import Blog

app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    b1 = Blog(title="初投稿", body="ORMを導入しました", user_name="yuki")
    db.session.add(b1)
    db.session.commit()
    print("完了！")