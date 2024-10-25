from flask import Flask
from config import Config

app = Flask('microblog', template_folder='templates')
app.config.from_object(Config)
from app import routes
