from random import randint
import time
class TicTacToe :
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.player = True
    
    def get_state(self):
        print(self.current_player)
        return {
            'board': self.board,
            'current_player': self.current_player,
            'winner': self.winner,
            'turn' : self.whoturn()
        }
    
    

    def make_move(self, row, col):
        if self.winner:
            raise ValueError("Game is over")
        
        if self.board[row][col] == ' ':
            self.board[row][col] = "X"
            self.current_player = 'O'
            self.turn()
            
            
        else:
            raise ValueError("Cell is already occupied")
        
        if self.won() is not None:
            self.winner = self.won()

        
    def won(self):
        horizontals = []
        verticals = []
        diagonals = []
        op_diagonals = []
        for i in range(3):
            diagonals.append(self.board[i][i])
            #print("This is diagonals",diagonals)
            op_diagonals.append(self.board[i][2-i])
            #print("This is op_diagonals",op_diagonals)
            horizontals.append([self.board[i][0], self.board[i][1], self.board[i][2]])
            #print("This is horizontals",horizontals)
            verticals.append([self.board[0][i], self.board[1][i], self.board[2][i]])
            #print("This is verticals",verticals)
        lines = horizontals + verticals + [diagonals] + [op_diagonals]
        print("This is lines",lines) 
        for line in lines:
            print("This is line",line) 
            if line[0] != ' ' and (line[0] == line[1] == line[2]):
                self.winner = line[0]
                return self.winner
            else :
                continue

    def turn(self) :
        if self.player == True:
            self.player = False
        else :
            self.player = True

    def whoturn(self) :
        return self.player
        
    def ai_move(self) :
        if self.player == True :
            return
        print("THIS IS AI MOVE")
        self.current_player = 'X'
        time.sleep(2)
        while True :
            xint = randint(0,2)
            yint = randint(0,2)

            if self.board[xint][yint] == ' ' :
                self.board[xint][yint] = 'O'
                self.turn()
                break
        if self.won():
            self.winner = self.won()
        
    

# game1 = TicTacToe()    
# game1.board = [['X', ' ', 'X'], ['X', ' ', ' '], [' ', ' ', ' ']]
# print(game1.won())
#print(TicTacToe().board)
