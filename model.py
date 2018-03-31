''' chess v3, Jansen Yan '''
class Board:
    def __init__(self, xDim, yDim):
        ''' make an 8 x 8 array '''
        self.xDim = xDim
        self.yDim = yDim
        self.board = [ ["*"] * self.xDim] * self.yDim
        
    def __str__(self):
        ''' print(Board object) should print board with algebraic notation'''
        boardStr = ""
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h"]
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        ''' print numbers on the side of the board '''
        
        for i in range(self.xDim):
            ''' start in reverse to get 8 first, then 7, 6, etc'''
            boardStr += str(numbers[-i-1]) + " "
            for j in range(self.yDim):
                boardStr += self.board[i][j] + " " 
            boardStr += "\n"
        boardStr += "  "
        for i in range(len(alphabet)):
            boardStr += alphabet[i] + " "
        return boardStr
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
        ## if pawn hasn't moved, it can move twice
        pass

b = Board(8,8)
print(b)
            
            
