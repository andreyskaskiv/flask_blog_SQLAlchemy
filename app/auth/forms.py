from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField("Email: ",
                        validators=[DataRequired(),
                                    Length(10, 100),
                                    Email()],
                        render_kw={'placeholder': 'Enter email'})

    password = PasswordField("Password: ",
                             validators=[DataRequired()],
                             render_kw={'placeholder': 'Enter password'})

    remember = BooleanField('Remember Me', default=False)

    submit = SubmitField("Login",
                         render_kw={'class': 'btn btn-success'})



class RegistrationForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(2, 100)],
        render_kw={'placeholder': 'Enter your name'})

    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 100), Email()],
                        render_kw={'placeholder': 'Enter email'})

    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('password_repeat', message='Passwords must match')],
                             render_kw={'placeholder': 'Enter password'})

    password_repeat = PasswordField('Confirm password',
                                    validators=[DataRequired()],
                             render_kw={'placeholder': 'Repeat password'})

    submit = SubmitField('Sign Up',
                         render_kw={'class': 'btn btn-success'})
