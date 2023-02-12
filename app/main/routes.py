from flask import render_template

from app.auth.models import Post
from app.main import main

@main.route('/')
def index():
    posts = Post.query.all()
    return render_template(
        'main/index.html',
        posts=posts,
        title='Home page')


@main.route('/about')
def about():
    title = "About"
    return render_template('about/about.html',
                           title=title)
