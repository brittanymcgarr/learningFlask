Installation dependencies:
    sudo apt-get install pip
*    pip install sqlalchemy
*    pip install flask-sqlalchemy
*    pip install flask-migrate
*    pip install Flask-Login
     pip install flask-bcrypt
*    pip install Flask-Admin

* Note that these entries must be configured for PyCharm by entering
    File >> Settings >> Project: UTM-Web >> Project Interpreter >> (+ on the side bar) >> Search: "SQLALchemy"
    From there, search for the Flask-SQLAlchemy, Flask-Login, and Flask-Migrate and install.

Other useful installations and debugging tools:
    ipython
    virtualenv

To Build Database:

To Migrate and Update Database:
    python manage.py db migrate
    python manage.py db upgrade

To Run from Console:
    in FlaskPractice/app directory:
         python manage.py runserver
