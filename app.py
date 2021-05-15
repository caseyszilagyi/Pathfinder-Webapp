from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send, emit
import json
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
socketio = SocketIO(app)

# Loads the page
@app.route('/')
def index():
    return render_template("index.html")


# Run when the start button is pressed
@socketio.on('start')
def start_program():
    print('Started program', file=sys.stderr)
    change_cell_coords(5, 5, "visited")


# Called from the front end to change a cell
@socketio.on('change_cell')
def change_cell_frontend(data):
    change_cell(data['ID'], data['type']);

# Call this method to change the cell to a different type. Calls method below by converting coordinates to proper format
# Currently implemented types are unvisited, visited, wall, path
def change_cell_coords(x, y, changeType):
    blockID = str(y) + ":" + str(x)
    change_cell(blockID, changeType)

## Called by the method above, will actually change the cell display on the front end
def change_cell(blockID, changeType):
    print("Change cell start")
    emit('change_cell', {'ID': blockID, 'type': changeType})
    print("Change cell end")


# Test method that prints whatever is need
@socketio.on('test')
def test(data):
    print("Test Callback, data: " + data["ID"], file=sys.stderr)



if __name__ == "__main__":
    socketio.run(app, debug=True)
    #app.run(debug=True)

