class TicTacToe :
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
    
    def get_state(self):
        return {
            'board': self.board,
            'current_player': self.current_player,
            'winner': self.winner
        }
    

    def make_move(self, row, col):
        if self.winner is not None:
            raise ValueError("Game is over")
        
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
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
        
        return None

# game1 = TicTacToe()    
# game1.board = [['X', ' ', 'X'], ['X', ' ', ' '], [' ', ' ', ' ']]
# print(game1.won())
#print(TicTacToe().board)
