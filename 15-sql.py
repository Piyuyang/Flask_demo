from flask import Flask

app = Flask(__name__)


class MySQLConfig(object):
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/toutiao"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


app.config.from_object(MySQLConfig)


