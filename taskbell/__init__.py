from flask import Flask
from flask_sqlalchemy import SQLAlchemy

print("__init__.pyがじっこうされました")
app = Flask(__name__)
print("appがつくられました")
app.config.from_object("taskbell.config")

db = SQLAlchemy(app)

# taskbell内の__init__ではviewsは定義されてなかったけど、フォルダ内のviews.pyを発見した
# views.pyを実行する
from taskbell import views
