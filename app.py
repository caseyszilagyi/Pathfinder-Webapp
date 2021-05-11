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

@app.route('/test')
def clickOnBox():
    print('box click call')
    return ("nothing")

@app.route('/update_block', methods = ['POST'])
def updateBlock():
    print('update block', file=sys.stderr)

@socketio.on('change_block_on_frontend')
def changeBlock(blockID, changeType):
    print("change block")
    data = {}
    data['ID'] = blockID
    data['type'] = changeType
    json_data = json.dumps(data)
    emit('change_block_on_frontend', data = json_data)

if __name__ == "__main__":
    socketio.run(app, debug=True)
    #app.run(debug=True)


#changeBlock("5:5", "visited")