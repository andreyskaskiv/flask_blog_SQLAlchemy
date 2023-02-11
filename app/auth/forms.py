from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

from app.auth.models import User


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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
