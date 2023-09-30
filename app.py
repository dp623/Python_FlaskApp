import os
from flask import Flask, request, render_template_string
from models import db, User

# Flask
app = Flask(__name__)

# DBパス(無ければ作成)
db_path = os.path.join(os.path.dirname(__file__), 'db')
db_file = 'sample.db'
os.makedirs(db_path, exist_ok=True)

# FlaskとSQLAlchemyを接続
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path +  '/' + db_file)
db.init_app(app)

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
