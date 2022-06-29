from flask import Flask
from flask_socketio import SocketIO, send, emit
from time import sleep
from random import randrange
cpt = 0
last_cpt = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'marouane_taloudi'
socketio = SocketIO(app, cors_allowed_origins="*", logge=True)
app.debug = True
app.host = 'localhost'


@socketio.on("message")
def handleMessage(msg):
    global cpt, last_cpt
    while True:
        socketio.sleep(3)
        if cpt == 0:
            continue
        n = str(randrange(2))
        if last_cpt != n:
            last_cpt = n
            print(n)
            send(n, broadcast=True)


@socketio.event
def connect():
    global cpt
    if cpt == 0:
        send('--.', broadcast=True)
    cpt += 1
    print("I'm connected!", cpt)


@socketio.event
def disconnect():
    global cpt
    cpt -= 1
    print("I'm disconnected!", cpt)


if __name__ == '__main__':
    socketio.run(app)
