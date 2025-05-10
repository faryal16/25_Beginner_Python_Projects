import random

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        
        self.board = self.make_new_board()
        self.assign_values_to_board()
        
        self.dug = set() # to keep track of places dug
        
    
    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size
            
            if board[row][col] == '*':
                continue
            
            board[row][col] = '*'
            bombs_planted += 1
            
        return board
    
    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self , row, col):
        num_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_bombs += 1
        return num_bombs
    
    def dig(self, row, col):
        self.dug.add((row, col))
        
        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col -1), min(self.dim_size, col +2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
                
        return True
    
    
    def __str__(self):
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r, c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = ' '
                    
        string_rep = ''
        widths = []
        for idx in range(self.dim_size):
            columns = [visible_board[row][idx] for row in range(self.dim_size)]
            widths.append(len(max(columns, key=len)))
            
        for i in range(self.dim_size):
            row = visible_board[i]
            string_rep += ' | '.join(f"{cell:>{widths[idx]}}" for idx, cell in enumerate(row))
            string_rep += '\n'
            
        return string_rep
    
def play(dim_size = 3, num_bombs = 3):
    board = Board(dim_size, num_bombs)
    
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        
        user_input = input("\nWhere would you like to dig? Input as row, col: ")
        try:
            row, col = map(int, user_input.split(','))
            if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
                raise ValueError
        except ValueError:
            print("\nInvalid input. Try again")
            continue
        
        safe = board.dig(row, col)
        if not safe:
            break
        
    if safe:
        print("\n🎉 CONGRATS! You won!")
        
    else:
        print("\n💥 Game Over! You hit a bomb.")
        board.dug= [(r, c) for  r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)



if __name__ == '__main__':
    play()
        