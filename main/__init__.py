import flask, os, mysql.connector
from flask_sqlalchemy import SQLAlchemy
app = flask.Flask(__name__)

#SECRET_KEY = os.urandom(32)
app.secret_key = "abcdefg"

db = mysql.connector.connect(
    host="104.168.136.69",
    user="yscbtlcv_cwkchi5781",
    passwd="singlebird5781!",
    database="BTSTRIVIA"
)


cursor = db.cursor()

from main import routes

