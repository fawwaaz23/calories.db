import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

# ✅ This line is the key
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db = SQLAlchemy(app)
