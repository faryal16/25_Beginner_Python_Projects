import streamlit as st
import copy

# --- 4x4 Sudoku Solver Logic ---

GRID_SIZE = 4
BOX_SIZE = 2

def run():
    def find_empty(board):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if board[i][j] == 0:
                    return i, j
        return None

    def is_valid(board, num, pos):
        row, col = pos
        if num in board[row]: return False
        if num in [board[i][col] for i in range(GRID_SIZE)]: return False

        box_x, box_y = col // BOX_SIZE, row // BOX_SIZE
        for i in range(box_y * BOX_SIZE, box_y * BOX_SIZE + BOX_SIZE):
            for j in range(box_x * BOX_SIZE, box_x * BOX_SIZE + BOX_SIZE):
                if board[i][j] == num:
                    return False
        return True

    def solve(board):
        empty = find_empty(board)
        if not empty:
            return True
        row, col = empty
        for num in range(1, GRID_SIZE + 1):
            if is_valid(board, num, (row, col)):
                board[row][col] = num
                if solve(board):
                    return True
                board[row][col] = 0
        return False

    def get_hint(board):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if board[i][j] == 0:
                    for num in range(1, GRID_SIZE + 1):
                        if is_valid(board, num, (i, j)):
                            return (i, j, num)
        return None

    # --- Streamlit UI ---

    # st.set_page_config(page_title="Mini Sudoku", page_icon="🧩", layout="centered")
    st.title("🧩 4x4 Mini Sudoku Solver")
    st.write("Use **0** for empty cells.")

    board_input = []
    for i in range(GRID_SIZE):
        cols = st.columns(GRID_SIZE)
        row = []
        for j in range(GRID_SIZE):
            val = cols[j].number_input("", 0, GRID_SIZE, 0, key=f"{i}-{j}", label_visibility="collapsed")
            row.append(val)
        board_input.append(row)

    col1, col2, col3 = st.columns(3)

    # Buttons
    if col1.button("🔍 Solve"):
        original = copy.deepcopy(board_input)
        board = copy.deepcopy(board_input)

        if solve(board):
            st.success("✅ Solved! See comparison below:")
            input_col, output_col = st.columns(2)
            input_col.markdown("### Your Input")
            output_col.markdown("### Solved Board")

            for i in range(GRID_SIZE):
                input_cells = input_col.columns(GRID_SIZE)
                solved_cells = output_col.columns(GRID_SIZE)
                for j in range(GRID_SIZE):
                    user_val = original[i][j]
                    solved_val = board[i][j]

                    # Input side
                    color_in = "#90EE90" if user_val == solved_val and user_val != 0 else (
                        "#FFB6C1" if user_val != 0 else "#f0f0f0")
                    input_cells[j].markdown(
                        f"<div style='text-align:center; padding:8px; background-color:{color_in}; "
                        f"border-radius:5px; font-size:20px; border:1px solid #ccc;'>"
                        f"{user_val if user_val != 0 else '-'}</div>",
                        unsafe_allow_html=True)

                    # Output side
                    solved_cells[j].markdown(
                        f"<div style='text-align:center; padding:8px; background-color:#f9f9f9; "
                        f"border-radius:5px; font-size:20px; border:1px solid #ccc;'>"
                        f"{solved_val}</div>",
                        unsafe_allow_html=True)
        else:
            st.error("❌ No solution found.")

    if col2.button("💡 Hint"):
        hint = get_hint(copy.deepcopy(board_input))
        if hint:
            i, j, num = hint
            st.info(f"Try placing **{num}** at row {i+1}, column {j+1}")
        else:
            st.warning("No valid hints available — puzzle may be complete.")

    if col3.button("🔄 Reset"):
        st.rerun()

if __name__ == " __main__":
    run()