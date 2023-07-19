from flask import Flask, render_template, url_for, request
from flask import Flask, render_template, url_for, flash, redirect
from sqlalchemy import create_engine
# this these are the forms that we are using
from forms import RegistrationForm, NewsArticleForm, LoginForm
from flask_behind_proxy import FlaskBehindProxy
# for SQL database intergration using sqlalchemy
# for dates
from datetime import datetime
# helps me get the current user and check if they are loggedInand then display pages accordingly
from flask_login import LoginManager, current_user, logout_user, login_user
from api_handler import get_pages
import pymysql.cursors  
from sqlalchemy import create_engine
# import os
# specifying tyhe directory names
# TEMPLATE_DIR = os.path.abspath('../templates')
# STATIC_DIR = os.path.abspath('../static')


app = Flask(__name__)

# database configuration
host = 'localhost'
user = 'notladi'
password = 'xeno6'
port = 3306
database = 'buzz'

conn = pymysql.connect(host=host, user=user, passwd=password, db=database, charset='utf8')

# Create an SQLAlchemy engine using the connection URI
engine = create_engine('mysql+pymysql://{user}:{password}@{host}:{port}/{database}'.format(
    user=user, password=password, host=host, port=port, database=database
))
# helps with redirects
proxied = FlaskBehindProxy(app)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# secret key to help with CRSF token
app.config['SECRET_KEY'] = '5a063a9f5f7a1769407c2c2066c5023e'

# I will have these models as a separate file/module that we will need to import
# User model

# User model


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=False, nullable=False)
#     password = db.Column(db.String(60), nullable=False)
#     is_active = db.Column(db.Boolean, default=True)

#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}')"

#     def get_id(self):
#         return str(self.id)


# with app.app_context():
#     db.create_all()


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=int(user_id), is_active=True).first()

# newsArticle model


# class NewsArticle(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False, unique=False)
#     content = db.Column(db.String(400), nullable=False, unique=False)
#     created_at = db.Column(db.DateTime, nullable=False,
#                            default=datetime.utcnow)
#     image = db.Column(db.String(255), nullable=False, unique=False)

#     def image_url(self):
#         return url_for('static', filename='images/' + self.image_filename)

#     def __repr__(self):
#         return f'<NewsArticle {self.id}>'


# routes section
@app.route('/')
@app.route('/home')
def home_page():
    pages = get_pages()
    # return render_template('index.html', pages=pages)
    return render_template('index.html', subtitle='Home Page', text='This is the home page', pages=pages)

# to create more pages we basically define a url route and then define the function for that


@app.route('/register', methods=['Get', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  # checks if entries are valid
        # Create a new User instance with the form data
        user = User(username=form.username.data, password=form.password.data)

        # Add the user to the database session
        db.session.add(user)

        # commit the changes to the database
        db.session.commit()
        login_user(user)  # Log in the newly registered user
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home_page'))  # if so - send to home page
    return render_template('register.html', title='Register', form=form)


@app.route('/profile')
def profile():
    return render_template('profile.html', subtitle='profile_page', text='info on the user')


# Login and logout logic


@login_manager.user_loader
def load_user(user_id):
    # Load the user object from the database based on the user_id
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Retrieve the user from the database based on the entered username
        user = User.query.filter_by(username=form.username.data).first()

        # Check if the user exists and the password is correct
        if user and user.password == form.password.data:
            login_user(user)  # Log in the user
            flash('Login successful!', 'success')
            return redirect(url_for('home_page'))
        else:
            flash('Invalid username or password.', 'danger')

    return render_template('login.html', subtitle='Login', form=form)


@app.route('/logout')
def logout():
    # Log out the user
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home_page'))

# this handles everything with the news articles
@app.route('/blogs', methods=['POST', 'GET'])
def blogs():
    return render_template('Blogs.html', subtitle='Blogs', text='This is the blogs page')


if __name__ == '__main__':
    app.run(debug=True, port=5010)
