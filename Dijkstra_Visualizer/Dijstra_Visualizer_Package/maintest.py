from main import *
from tile import *

tilelist = initialize(28,60)
setstart(10,10)
setend(20,20)
calculateDistancesfrom()

tile1adjacencylist = tilelist[1].getadjacencylist()

shortestpath = getDijkstraPathTo()

#print("Tile 1 Adjacency List: \n")
#for current in tile1adjacencylist:
#    xcoordinate = current.getx()
#    ycoordinate = current.gety()
#    print("(",xcoordinate, ", ", ycoordinate,")")
#
#print("")

print("Shortest Path: \n")

for current in shortestpath:
    xcoordinate = current.getx()
    ycoordinate = current.gety()
    print("(",xcoordinate, ", ", ycoordinate,")")