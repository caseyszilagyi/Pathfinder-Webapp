from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send, emit
import json
import sys

import main
import tile


import logging
import time
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
socketio = SocketIO(app)

main.initialize(60, 28)

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


# Run when the start button is pressed
@socketio.on('start')
#def start_program(startx, starty, endx, endy):

def start_program(data):
    print('Started program', file=sys.stderr)
    print("startend" + data['start'] + data['end'])
    start = data['start'].split(":")
    end = data['end'].split(":")

    main.initialize(60, 28)
    main.setstart(int(start[1]), int(start[0]))
    main.setend(int(end[1]) ,int(end[0]))


    visitedlist = main.calculateDistancesfrom()
    pathlist, finaldistance = main.getDijkstraPathTo()

    currentdistancevisited = 0

    while currentdistancevisited < finaldistance:

        for tile in visitedlist:
            if tile.getdistance() == currentdistancevisited:
                x = tile.getx()
                y = tile.gety()

                change_cell_coords(x,y,"visited")
        currentdistancevisited += 1
        time.sleep(0.1)

    for tile in pathlist:
        x = tile.getx()
        y = tile.gety()

        change_cell_coords(x,y,"path")
        time.sleep(0.02)



# Called from the front end to change a cell
# Called by the front end to change cell to aflask r wall
@socketio.on('change_cell')
def change_cell_frontend(data):
    change_cell(data['ID'], data['type'])
    coordinates = data['ID'].split(':')
    y = int(coordinates[0])
    x = int(coordinates[1])
    print(x)
    print(y)
    main.create_wall(x,y)

# Call this method to change the cell to a different type. Calls method below by converting coordinates to proper format
# Currently implemented types are unvisited, visited, wall, path

def change_cell_coords(x, y, changeType):
    blockID = str(y) + ":" + str(x)
    change_cell(blockID, changeType)

## Called by the method above, actually will change the cell display on the front end
# Called by the other methods to send to the front end
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

def set_end(x,y):
    setstart(x,y)

def set_start(x,y):
    setend(x,y)

