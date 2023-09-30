Flask, SQLite, および SQLAlchemy を用いた簡単な CRUD（Create, Read, Update, Delete）アプリケーションのサンプルコードを以下に示します。

## 1. プロジェクトのセットアップ
~~~
mkdir flask_sqlalchemy_example
cd flask_sqlalchemy_example
python -m venv venv
source venv/bin/activate  # Windowsの場合は venv\Scripts\activate
pip install flask flask_sqlalchemy
~~~
## 2. プロジェクト構成
~~~
flask_sqlalchemy_example/
  |- app.py
  |- models.py
~~~
## 3. app.py
app.py ファイルを作成し、以下のコードを記述してください。
~~~
from flask import Flask, request, render_template_string
from models import db, User
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    users = User.query.all()
    return render_template_string('''
        <form method="post" action="/add_user">
            <input type="text" name="username" placeholder="Username" required>
            <button type="submit">Add User</button>
        </form>
        <ul>
            {% for user in users %}
                <li>{{ user.username }}</li>
            {% endfor %}
        </ul>
    ''', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form.get('username')
    user = User(username=username)
    db.session.add(user)
    db.session.commit()
    return 'User added.', 200


if __name__ == '__main__':
    app.run(debug=True)
~~~
## 4. models.py
models.py ファイルを作成し、以下のコードを記述してください。
~~~
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
~~~
## 5. 実行
コマンドラインで以下のコマンドを実行してください。
~~~
python app.py
~~~
これにより、http://127.0.0.1:5000/ にアクセスすることで、ユーザーを追加できるようになります。

このコードは単純な例であり、実際のプロジェクトでは適切なエラーハンドリング、フォームバリデーション、セキュリティ対策（たとえば CSRF 対策）を行う必要があります。