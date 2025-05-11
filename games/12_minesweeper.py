import streamlit as st
import random

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row, col = divmod(loc, self.dim_size)
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

    def get_num_neighboring_bombs(self, row, col):
        num_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if (r, c) == (row, col):
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
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if (r, c) not in self.dug:
                    self.dig(r, c)
        return True

def run():
    st.title("💣 Minesweeper")

    if "board" not in st.session_state:
        dim = st.number_input("Grid size", min_value=3, max_value=10, value=5)
        bombs = st.number_input("Number of bombs", min_value=1, max_value=dim*dim - 1, value=5)
        if st.button("Start Game"):
            st.session_state.board = Board(dim, bombs)
            st.session_state.game_over = False
            st.session_state.won = False
            st.rerun()
        return

    board = st.session_state.board

    # SAFEGUARD
    if not isinstance(board, Board):
        st.warning("Session data was corrupted. Restarting...")
        del st.session_state.board
        st.rerun()

    dim_size = board.dim_size

    for row in range(dim_size):
        cols = st.columns(dim_size)
        for col in range(dim_size):
            cell = (row, col)
            revealed = cell in board.dug or st.session_state.game_over

            if revealed:
                val = board.board[row][col]
                label = "💣" if val == '*' else str(val) if val != 0 else " "
            else:
                label = "⬜"

            if cols[col].button(label, key=f"{row}-{col}", disabled=revealed):
                safe = board.dig(row, col)
                if not safe:
                    st.session_state.game_over = True
                    st.error("💥 You hit a bomb! Game Over.")
                elif len(board.dug) == dim_size**2 - board.num_bombs:
                    st.session_state.won = True
                    st.success("🎉 You won!")
                st.rerun()

    if st.button("🔁 Restart"):
        for key in ["board", "game_over", "won"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

if __name__ == '__main__':
    run()
