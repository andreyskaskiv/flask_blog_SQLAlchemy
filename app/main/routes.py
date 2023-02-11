from flask import render_template

from app.main import main

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@main.route('/')
def index():
    return render_template(
        'main/index.html',
        posts=posts,
        title='Home page')


@main.route('/blog')
def about():
    title = "About"
    return render_template('about/about.html',
                           title=title)
