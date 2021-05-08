class tile:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;


class wall(tile):
    pass

class nonwall(tile):
    pass

class path(tile):
    pass
