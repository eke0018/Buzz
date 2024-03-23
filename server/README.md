# Buzz - Newspaper Website with Flask

Buzz is a newspaper website built using Python and Flask. It allows users to register, log in, view news articles, and play a Hangman game. The website features user authentication, database integration with SQLAlchemy, and interaction with the Discord API.

## Technologies Used

- Python
- Flask
- SQLAlchemy
- Discord4J
- HTML/CSS
- JavaScript

## Features

- User registration and login
- View and create news articles
- Edit and delete news articles
- View weather information
- Play Hangman game
- Discord integration for multiplayer Hangman
- Responsive design for different devices

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up a virtual environment if necessary.
4. Run the Flask application by executing `python app.py`.
5. Access the website through your browser at `http://localhost:5041`.

## Database Setup

- Buzz uses SQLite as its database. The database file (`new_db01.db`) will be created automatically when you run the application.
- You can modify the database configuration in `app.py` if needed.


## Customization

- Customize the website's appearance and functionality by modifying the HTML/CSS templates and Flask routes.
- Modify the Hangman game logic and word list according to your preferences.

## Folder Structure

- `templates`: HTML templates for rendering web pages.
- `static`: Static files such as CSS stylesheets, images, and JavaScript scripts.
- `forms.py`: Flask-WTF forms for user registration, login, and news article creation.
- `api_handler.py`: Integration with external APIs for weather information and Discord.
- `new_db01.db`: SQLite database file.
- `app.py`: Main Flask application file containing routes and database models.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
 
