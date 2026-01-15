from flask import Blueprint, render_template
from flaskr.models import Blog

bp = Blueprint('blog', __name__)

@bp.route('/blogs')
def index():
    blogs = Blog.query.all() # データベースから全取得
    return render_template('blog/index.html', blogs=blogs)