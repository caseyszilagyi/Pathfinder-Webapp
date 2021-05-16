from main import *
from tile import *

tilelist = initialize(60,28)
setstart(50, 25)
setend(15,15)
y = calculateDistancesfrom()

tile1adjacencylist = tilelist[119].getadjacencylist()

shortestpath,x = getDijkstraPathTo()

#print("Tile 60 Adjacency List: \n")
#for current in tile1adjacencylist:
#    xcoordinate = current.getx()
#    ycoordinate = current.gety()
#    print("(",xcoordinate, ", ", ycoordinate,")")

#print("")

print("Shortest Path: \n")

for current in shortestpath:
    xcoordinate = current.getx()
    ycoordinate = current.gety()
    print("(",xcoordinate, ", ", ycoordinate,")")
print("\n")
for tile in y:
    xcoord = tile.getx()
    ycoord = tile.gety()
    distance = tile.getdistance()
    iswall = tile.getwall()
    print("(",xcoord, ", ", ycoord,")"," Distance: ", distance, " Wall: ", iswall)