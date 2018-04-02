''' chess v3, Jansen Yan '''
#!/bin/env python3.0
### import ###
import re

### Global Variables ###

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h"]
NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8]
ORDER = {"R", "N", "B", "Q", "K", "B", "K", "R"}
BLACK = "B"
WHITE = "W"

### REGEX PATTERNS ###
ALGEBRAIC_REGEX = "^([rRbBkKqQnN])?([a-h])([1-8])$"

### Only to be used within these classes ###
class UI:
    def __init__(self):
        self.player1Color = ""
        self.player2Color = ""
        self.game = Gamestate()
    def setup(self):

        while (True):
            playerColor = raw_input('''Play as White or Black?
                                    Type W for White or B for Black: 
                                \n''')
            if playerColor in ["B", "b", "black", "Black"]:
                self.player1Color = BLACK
                self.player2Color = WHITE
                break
            elif playerColor in ["W", "w", "white", "White"]:
                self.player1Color = WHITE
                self.player2Color = BLACK
                break
            else:
                print("Incorrect Input, please enter W or B")
        self.game.initPlayers(player1Color, player2Color)
  
    def gameLoop(self):

        ## if game is not over
        ## find out who's turn it is
        ## ask for the player's input

        while (not self.game.isGameOver):
            currentTurn = self.game.getCurrentTurn()
            notation = raw_input(currentTurn + " : please input algebraic notation\n ")
            gameCoords = self.processPlayerInput(
        
        
        
    def processPlayerInput(self, playerInput):
        ## given the current player's turn, return the gamestate coordinates
        
        match = re.search(ALGEBRAIC_REGEX, playerInput)
        ## if the input is valid
        if (self.isValidPlayerInput(match)):
            ## transpose the algebraic coordinates into gamestate coordinates (2D array)
            return self.transpose(match)
            
    def isValidPlayerInput(self, matchObject):
        ''' helper function to process proper algebraic notation '''
        if (matchObject):
            return True
        return False

    def transpose(self, matchObject):
        ## returns a tuple of the 2D board coordinates
        pass
        

class Gamestate:
    def __init__(self):
        self.board = Board()
        self.turn = Turn()
        self.P1 = None
        self.P2 = None
        ## allPieces is a map where keys are pieces and values are coordinates as tuples
        self.allPieces = {}
        
    def initBoard(self):
        pass
    
    def initPlayers(self, P1Color, P2Color):
        self.P1 = Player().setColor(P1Color)
        self.P2 = Player().setColor(P2Color)
        
    def isGameOver(self):
        if (allPieces["WK"].isCheckMate() or allPieces["BK"].isCheckMate()):
            return True
        return False
    
    def getCurrentTurn(self):
        return self.turn.getTurn()
    
    def changeTurn(self):
        self.turn.changeTurn()
    

class Player:
    def __init__(self):
        self.capturedPieces = []
        self.color = ""
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    
class Turn:
    def __init__(self):
        self.turn = WHITE
        
    def changeTurn(self):
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE
            
    def getTurn(self):
        return self.turn
    
class Board:
    def __init__(self, xDim, yDim):
        ''' make an 8 x 8 array '''
        self.xDim = xDim
        self.yDim = yDim
        self.board = [ ["*"] * self.xDim] * self.yDim
        
    def __str__(self):
        ''' print(Board object) should print board with algebraic notation'''
        boardStr = ""
        
        ''' print numbers on the side of the board '''
        
        for i in range(self.xDim):
            ''' start in reverse to get 8 first, then 7, 6, etc'''
            boardStr += str(NUMBERS[-i-1]) + " "
            for j in range(self.yDim):
                boardStr += self.board[i][j] + " " 
            boardStr += "\n"
        boardStr += "  "
        for i in range(len(ALPHABET)):
            boardStr += ALPHABET[i] + " "
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

    def isPromotion(self):
        pass

    def isEnPassant(self):
        pass
    
class Knight(Piece):
    def checkValidMove(self, x, y):
        pass
    
class Bishop(Piece):
    def checkValidMove(self, x, y):
        pass
    
class Rook(Piece):
    def checkValidMove(self, x, y):
        pass

class Queen(Piece):
    def checkValidMove(self, x, y):
        pass

class King(Piece):
    def __init__(self):
        Piece.__init__()
        self.hasMoved = False
    def checkValidMove(self, x, y):
        pass
    def isCheck(self):
        pass
    def isCheckMate(self):
        pass
    def canCastle(self):
        pass
    
b = Board(8,8)
print(b)
            
            
