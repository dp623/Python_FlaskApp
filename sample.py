import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask
app = Flask(__name__)

# DBパス(無ければ作成)
db_path = os.path.join(os.path.dirname(__file__), 'db')
db_file = 'sample.db'
os.makedirs(db_path, exist_ok=True)

# FlaskとSQLAlchemyを接続
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path +  '/' + db_file)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

with app.app_context():
    # DBファイル作成
    db.create_all()