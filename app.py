import os

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from repository.db.database    import db
from repository.models.message import Message

# from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)

# Variaveis do APP
app.config['SECRET_KEY']              = "developBySantiro_2024-10-09"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('DATABASE')

db.init_app(app)

# Iniciando o database
socketio = SocketIO(app)

@app.route('/chat')
def index():
    messages = Message.query.all()
    print(messages)
    print("Nova pessoa Conectou no chat")
    return render_template('index.html', messages=[{'message_id': message.message_id, 'message': message.message} for message in messages])


@socketio.on('message')
# @login_required
def handle_message(msg):
    emit('message', msg, broadcast=True, callback=Message.add_message(message=msg))


if __name__ == '__main__':
    socketio.run(app, debug=True)
