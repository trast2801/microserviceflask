import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'никогда не наступит этот день'