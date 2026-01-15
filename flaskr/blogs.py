from flask import Blueprint, render_template, request, redirect, url_for, flash
from flaskr import db
# models.pyのBlogクラスをインポート
from flaskr.models import Blog

blog_bp = Blueprint('blogs', __name__, url_prefix='/blogs')

# 一覧表示
@blog_bp.route('/')
def index():
    blogs = Blog.query.order_by(Blog.created_at.desc()).all()
    return render_template('blogs/index.html', blogs=blogs)

# 新規投稿フォーム表示と投稿処理
@blog_bp.route('/new', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        user_name = request.form['user_name']

        # Blogインスタンスを作成
        new_blog = Blog(title=title, body=body, user_name=user_name)
        # バリデーションを実行
        errors = new_blog.validate()

        # エラーがあればフォームに戻して表示する
        if errors:
            # エラーのリストの要素一つずつをflushに入れている
            for e in errors:
                flash(e, 'error')
            return render_template('blogs/new.html', title=title, body=body, user_name=user_name)
        # DBへ保存
        db.session.add(new_blog)
        db.session.commit()

        # 保存後、詳細ページへリダイレクト
        return redirect(url_for('blogs.detail', blog_id=new_blog.id))

    # blogs/new.htmlをテンプレートとしてHTMLを組み立てる
    return render_template('blogs/new.html')

# 詳細ページ
@blog_bp.route('/<int:blog_id>')
def detail(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template('blogs/detail.html', blog=blog)

# 編集ページ (表示と更新処理) を付け加え
@blog_bp.route('/<int:blog_id>/edit', methods=['GET', 'POST'])
def edit(blog_id):
    # 編集対象のデータを取得
    blog = Blog.query.get_or_404(blog_id)

    if request.method == 'POST':
        # フォームから送られた内容で既存データを上書き
        blog.title = request.form['title']
        blog.body = request.form['body']
        blog.user_name = request.form['user_name']

        # バリデーションを実行
        errors = blog.validate()
        if errors:
            for e in errors:
                flash(e, 'error')
            return render_template('blogs/edit.html', blog=blog)

        # DBの変更を確定（更新時はdb.session.addは不要です）
        db.session.commit()
        
        flash('ブログを更新しました！', 'success')
        # 更新後は詳細ページへ移動
        return redirect(url_for('blogs.detail', blog_id=blog.id))

    # GETリクエスト時は現在のデータを編集フォーム(edit.html)に表示
    return render_template('blogs/edit.html', blog=blog)