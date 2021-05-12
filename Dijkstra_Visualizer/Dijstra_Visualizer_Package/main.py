import tile
import queue

tilelist = []
starttile = None
endtile = None

def calculateDistancesfrom(startx, starty):

    setstart(startx, starty)

    tilequeue = queue.Queue()
    visitedlist = []

    for nonwall in tilelist:

        nonwall.setdistance(float('inf'))
        nonwall.setvisited(False)
        tilequeue.put(nonwall)

    starttile.setdistance(0)
    starttile.setprev(None)
    tilequeue.put(starttile)


    while tilequeue.qsize() != 0:

        currenttile = tilequeue.get()
        visitedlist.append(currenttile)
        currenttiledistance = currenttile.getdistance()
        adjacencylist = currenttile.getadjacencylist()

        for adjacenttile in adjacencylist:

            adjacenttiledistance = adjacenttile.getdistance()
            iswall = adjacenttile.getwall()

            if adjacenttiledistance == float('inf') and iswall == False:

                adjacenttile.setdistance(currenttiledistance + 1)
                adjacenttile.setprev(currenttile)
                tilequeue.put(adjacenttile)

    return visitedlist

def getDijkstraPathTo(endx, endy):

    setend(endx, endy)

    temp = endtile


    pathlist = []


    while temp.getprev() != None:
        prev = temp.getprev()
        pathlist.append(prev)
        temp = prev


    list.reverse(pathlist)


    return pathlist

def initialize(gridwidth, gridheight):

    global tilelist

    y = 0

    while y < gridheight:

        x = 0

        while x < gridwidth:

            currenttile = tile.tile(x,y, float('inf'), None, None, False)
            x += 1
            tilelist.append(currenttile)

        y += 1

    for i in range(0,1680):

        above = i - 28
        below = i + 28
        left = i - 1
        right = i + 1

        if above > -1 and above < 1680:

            currenttile_adjacencylistabove = tilelist[i].getadjacencylist()
            currenttile_adjacencylistabove.append(tilelist[i-28])
            tilelist[i].setadjacencylist(currenttile_adjacencylistabove)

        if below > -1 and below < 1680:

            currenttile_adjacencylistbelow = tilelist[i].getadjacencylist()
            currenttile_adjacencylistbelow.append(tilelist[i + 28])
            tilelist[i].setadjacencylist(currenttile_adjacencylistbelow)

        if left > -1 and left < 1680:

            currenttile_adjacencylistleft = tilelist[i].getadjacencylist()
            currenttile_adjacencylistleft.append(tilelist[i - 1])
            tilelist[i].setadjacencylist(currenttile_adjacencylistleft)

        if right > -1 and right < 1680:

            currenttile_adjacencylistright = tilelist[i].getadjacencylist()
            currenttile_adjacencylistright.append(tilelist[i + 1])
            tilelist[i].setadjacencylist(currenttile_adjacencylistright)


    return tilelist

def setstart(startx, starty):
    global starttile
    for currenttile in tilelist:

        if (currenttile.getx() == startx and currenttile.gety() == starty):
            starttile = currenttile

    return

def setend(endx, endy):
    global endtile
    for currenttile in tilelist:
        if (currenttile.getx() == endx and currenttile.gety() == endy):
            endtile = currenttile

    return

def create_wall(x,y):
    for currenttile in tilelist:
        if (currenttile.getx() == x and currenttile.gety() == y):
            currenttile.setwall(true)

    return