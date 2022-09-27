import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@mysql/assignment?charset=utf8mb4'

SQLALCHEMY_TRACK_MODIFICATIONS = False

YOU_TUBE_DATA_API_KEY = ''

PER_PAGE_LIMIT = 12
