import os
from datetime import timedelta
from decouple import config

database  = config('DB_TYPE')
username  = config('DB_USER')
password  = config('DB_PASSWORD')
host      = config('DB_HOST')
port      = config('DB_PORT')
db_name   = config('DB_NAME')


class Config:
    SECRET_KEY = config('SECRET_KEY', 'secret')
    JWT_SECRET_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"{database}://{username}:{password}@{host}:{port}/{db_name}"