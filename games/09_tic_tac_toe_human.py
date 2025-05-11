import streamlit as st

def run():
    st.subheader("❌⭕ Human vs Human Tic-Tac-Toe")

    # Initialize board in session state
    if "board" not in st.session_state:
        st.session_state.board = [" "] * 9
        st.session_state.current_player = "X"
        st.session_state.game_over = False
        st.session_state.winner = None

    def check_winner(b, player):
        win_combos = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # columns
            [0,4,8], [2,4,6]            # diagonals
        ]
        return any(all(b[i] == player for i in combo) for combo in win_combos)

    def is_tie():
        return " " not in st.session_state.board

    def make_move(index):
        if st.session_state.board[index] == " " and not st.session_state.game_over:
            st.session_state.board[index] = st.session_state.current_player
            if check_winner(st.session_state.board, st.session_state.current_player):
                st.session_state.game_over = True
                st.session_state.winner = st.session_state.current_player
            elif is_tie():
                st.session_state.game_over = True
            else:
                # Switch player
                st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"

    def reset_game():
        st.session_state.board = [" "] * 9
        st.session_state.current_player = "X"
        st.session_state.game_over = False
        st.session_state.winner = None

    st.markdown("#### Positions:")
    st.text("| 0 | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |")

    st.write(f"**Current Player: {st.session_state.current_player}**")

    # Display board with buttons
    cols = st.columns(3)
    for i in range(9):
        with cols[i % 3]:
            if st.button(st.session_state.board[i] if st.session_state.board[i] != " " else " ", key=i):
                make_move(i)

    # Show game result
    if st.session_state.game_over:
        if st.session_state.winner:
            st.success(f"🎉 {st.session_state.winner} wins the game!")
        else:
            st.info("It's a tie!")

        if st.button("Play Again"):
            reset_game()

if __name__ == " __main__":
    run()