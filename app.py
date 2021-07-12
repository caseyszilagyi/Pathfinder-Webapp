from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send, emit

import main
import tile
import logging
import time
import sys
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
socketio = SocketIO(app)

main.initialize(60, 28)

#resetting instance variable to break out of start_program
resetting = False

# Loads the starting page
@app.route('/')
def index():
    return render_template("index.html")

# Run when the start button is pressed
@socketio.on('start')
def start_program(data):
    start = data['start'].split(":")
    end = data['end'].split(":")

    main.setstart(int(start[1]), int(start[0]))
    main.setend(int(end[1]) ,int(end[0]))


    visitedlist = main.calculateDistancesfrom()
    pathlist, finaldistance = main.getDijkstraPathTo()

    currentdistancevisited = 0


    while currentdistancevisited < finaldistance+1:

        if resetting == True:

            exit()

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



# Called from the front end to change a cell to a wall
@socketio.on('make_wall')
def make_wall(data):
    change_cell(data['ID'], data['type'])
    coordinates = data['ID'].split(':')
    x = int(coordinates[1])
    y = int(coordinates[0])
    main.create_wall(x,y)

# Call this method to change the cell to a different type. Calls method below by converting coordinates to proper format
# Currently implemented types are unvisited, visited, wall, path
def change_cell_coords(x, y, changeType):
    blockID = str(y) + ":" + str(x)
    change_cell(blockID, changeType)

# Called by the other methods to send change information to the front end. Use the method change_cell_coords for clarity
def change_cell(blockID, changeType):
    emit('change_cell', {'ID': blockID, 'type': changeType})


@socketio.on('reset')
def reset():
    ## TODO: Implement resetting

    global resetting

    resetting = True
    main.reset()
    for x in range(60):
        for y in range(28):
            change_cell_coords(x,y,"unvisited")
    print("reset")
    resetting = False



if __name__ == "__main__":
    socketio.run(app, debug=True)

def set_end(x,y):
    setstart(x,y)

def set_start(x,y):
    setend(x,y)
