from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    interests = StringField('Interests')
    submit = SubmitField('Sign Up')


class NewsArticleForm(FlaskForm):
    title = StringField('Title', validators=[
                        DataRequired(), Length(min=2, max=40)])
    content = TextAreaField('Content', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')
