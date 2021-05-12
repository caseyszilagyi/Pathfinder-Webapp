from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send, emit
import json
import sys
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/boxclick')
def clickOnBox():
    print('box click call', file=sys.stderr)
    return ("nothing")

@app.route('/update_block', methods = ['POST'])
def updateBlock():
    print('Update block', file=sys.stderr)

@socketio.on('start')
def start_program():
    print('Started program', file=sys.stderr)
    change_cell("5:5", "visited")

@socketio.on('test')
def test(data):
    print("Test Callback, data: " + data["ID"], file=sys.stderr)


def change_cell(blockID, changeType):
    print("Change cell start")
    emit('change_cell', {'ID': blockID, 'type': changeType})
    print("Change cell end")

if __name__ == "__main__":
    socketio.run(app, debug=True)
    #app.run(debug=True)

