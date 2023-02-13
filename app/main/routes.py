from flask import render_template, request

from app.auth.models import Post
from app.main import main


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)

    return render_template(
        'main/index.html',
        posts=posts,
        title='Home page')


@main.route('/about')
def about():
    title = "About"
    return render_template('about/about.html',
                           title=title)
