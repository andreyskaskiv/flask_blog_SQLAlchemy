from flask import render_template, redirect, flash, url_for

from app.auth import auth
from app.auth.forms import LoginForm,  RegistrationForm


@auth.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('auth/login.html',
                           title='Login',
                           form=form)




@auth.route("/register", methods=("POST", "GET"))
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.index'))

    return render_template('auth/register.html',
                           title='Register',
                           form=form)
