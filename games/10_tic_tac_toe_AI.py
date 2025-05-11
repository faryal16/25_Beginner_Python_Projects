import streamlit as st

PLAYER = 'X'
AI = 'O'
EMPTY = ' '

def run():
    class TicTacToe:
        def __init__(self):
            self.board = [[EMPTY for _ in range(3)] for _ in range(3)]
            
            
        def print_board(self):
            return "\n".join([" | ".join(row) for row in self.board])
        
        def player_move(self, row, col):
            if self.board[row][col] == EMPTY:
                self.board[row][col] = PLAYER
                
        def ai_move(self):
            _, move = self.minimax(self.board, True)
            if move:
                row, col = move
                self.board[row][col] = AI
                
        def minimax(self, board, is_maximizing):
            if self.check_winner(board, AI):
                return 1, None
            
            if self.check_winner(board, PLAYER):
                return -1, None
            
            if self.is_draw(board):
                return 0, None
            
            
            best_score = float('-inf') if is_maximizing else float('inf')
            best_move = None
            
            
            for i in range(3):
                for j in range(3):
                    if board[i][j] == EMPTY:
                        board[i][j] = AI if is_maximizing else PLAYER
                        score, _ = self.minimax(board, not is_maximizing)
                        board[i][j] = EMPTY
                        
                        if is_maximizing:
                            if score > best_score:
                                best_score = score
                                best_move = (i,j)
                                
                        else:
                            if score < best_score:
                                best_score = score
                                best_move = (i, j)
                                
            return best_score, best_move
        
        
        
        def check_winner(self, board, player):
            for i in range(3):
                if all([cell == player for cell in board[i]]) or \
                all([board[j][i] == player for j in range(3)]):
                    return True
            
            if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
                return True
            return False
        
        def is_draw(self, board):
            return all(cell != EMPTY for row in board for cell in row)
        
        def start_game(self):
            st.title("Tic-Tac-Toe 🎮 (vs Unbeatable AI)")
            st.write("Try to beat the unbeatable AI! You play as ❌, AI plays as ⭕")


            # Session state to keep track of the board
            if 'board' not in st.session_state:
                st.session_state.board = [[EMPTY for _ in range(3)] for _ in range(3)]
                st.session_state.game_over = False
                st.session_state.message = ""

            self.board = st.session_state.board

            # Display buttons in a grid
            for i in range(3):
                cols = st.columns(3)
                for j in range(3):
                    if self.board[i][j] == EMPTY and not st.session_state.game_over:
                        if cols[j].button(" ", key=f"{i}-{j}"):
                            self.player_move(i, j)
                            if self.check_winner(self.board, PLAYER):
                                st.session_state.message = "You Win! 🎉🎉🎉"
                                st.session_state.game_over = True
                                st.balloons()
                            elif self.is_draw(self.board):
                                st.session_state.message = "It's a draw!"
                                st.session_state.game_over = True
                            else:
                                self.ai_move()
                                if self.check_winner(self.board, AI):
                                    st.session_state.message = "AI wins! 🤖"
                                    st.session_state.game_over = True
                                elif self.is_draw(self.board):
                                    st.session_state.message = "It's a draw!"
                                    st.session_state.game_over = True
                    else:
                        cols[j].button(self.board[i][j], key=f"{i}-{j}", disabled=True)

            if st.session_state.message:
                st.markdown(f"## {st.session_state.message}")

            # Restart button
            if st.button("🔁 Restart Game"):
                st.session_state.board = [[EMPTY for _ in range(3)] for _ in range(3)]
                st.session_state.game_over = False
                st.session_state.message = ""
            
                
    
    game = TicTacToe()
    game.start_game()  
        
if __name__ == "__main__":
    run()