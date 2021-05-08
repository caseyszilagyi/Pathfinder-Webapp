class tile:

    def __init__(self,x,y, dist, visited, prev, wall):
        self.x = x
        self.y = y
        self.dist = dist
        self.visited = visited
        self.prev = prev
        self.wall = wall
        self.adjacencylist = []

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def setdistance(self, distance):
        self.dist = distance

    def setvisited(self, visited):
        self.visited = visited

    def setprev(self, prev):
        self.prev = prev

    def setwall(self, wall):
        self.wall = wall

    def setadjacencylist(self,adjacencylist):
        self.adjacencylist = adjacencylist

    def getdistance(self):
        return self.dist

    def getvisited(self):
        return self.visited

    def getprev(self):
        return self.prev

    def getwall(self):
        return self.wall

    def getadjacencylist(self):
        return self.adjacencylist

