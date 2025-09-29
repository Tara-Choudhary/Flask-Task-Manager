import os

MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'Tara%401234')
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')  # use localhost
MYSQL_DB = os.getenv('MYSQL_DB', 'taskdb')
MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
