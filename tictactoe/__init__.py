import os
from flask import Flask
from flask_cors import CORS

DATABASE = os.getenv("DATABASE_URL", "sqlite:///games.db")

app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources=r'/*', allow_headers="Content-Type")


import tictactoe.views