from flask import Blueprint, render_template
from flaskr.models import Blog # Blogクラスをインポート

blog_bp = Blueprint("blog", __name__)

@blog_bp.route("/blogs")
def blogs():
    # SQLを直接書かずに、モデルを使って全データを取得（投稿日時の降順）
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('blogs.html', blogs=blogs)