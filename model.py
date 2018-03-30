''' chess v3, Jansen Yan '''

class Piece:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.color = ""
        
        
    def setCoord(self, x, y):
        self.x = x
        self.y = y
        
    def getCoord(self):
        return (self.x, self.y)
    
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color

class Pawn(Piece):
    def __init__(self):
        Piece.__init__()
        self.hasMoved = False
        
    def checkValidMove(self, x, y):
        ## if color is white, allow move twice
        if self.color == "W":
            
    
