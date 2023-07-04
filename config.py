import os

# SQLAlchemy configuration
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:shahg12-@localhost:3306/flask-sql-crud'
JWT_SECRET_KEY = 'my_secret'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Other app configurations
DEBUG = True  # Set to False in production
