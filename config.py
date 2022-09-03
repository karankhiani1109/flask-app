import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://karan:password@localhost/assignment?charset=utf8mb4'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

YOU_TUBE_DATA_API_KEY = 'AIzaSyB6_8ULZDIhVMGEogqAne_PNhZSk7TpgR0'