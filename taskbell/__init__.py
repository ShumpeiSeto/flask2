# coding: utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import locale


print("__init__.pyがじっこうされました")
app = Flask(__name__)
print("appがつくられました")
# config file別途作成している

app.config.from_object("taskbell.config")
app.secret_key = "abcdefghijk"

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# dbできた後でモデルをインポート
from taskbell.models.add_task import Tasks
from taskbell.models.login_user import User


# 言語設定のためのカスタムフィルター書いてみる
@app.template_filter("add_weekday")
def str_add_weekday(date):
    weekdays = ["月", "火", "水", "木", "金", "土", "日"]
    weekday = weekdays[date.weekday()]
    return f"{date.strftime('%m/%d')}({weekday})"

@app.template_filter("convert_importance")
def str_convert_importance(num_importance):
    importances = ["低", "中", "高"]
    importance = importances[num_importance]
    return importance

# Migration 設定
migrate = Migrate(app, db)

# views.pyを実行する
from taskbell import views
