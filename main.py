import streamlit as st
import importlib

# Set page config
st.set_page_config(page_title="Game Arcade", page_icon="🎮", layout="wide")

# --- Game list ---
games = {
    "📖 Mad Libs": "games.01_mad_libs",
    "🔢 Guess the Number (computer)": "games.02_guess_num_computer",
    "🧮 Guess the Number (user)": "games.03_guess_user",
    "✊✋✌️ Rock, Paper, Scissors": "games.04_rock_paper_scissors",
    "🕴 Hangman": "games.05_hangman",
    "⏳ Countdown Timer": "games.06_countdown_timer",
    "🔑 Password Generator": "games.07_password_generator",
    "📱 QR Code Encoder / Decoder": "games.08_qr_code",
    "❌ Tic-Tac-Toe": "games.09_tic_tac_toe_human",
    "🤖 Tic-Tac-Toe AI": "games.10_tic_tac_toe_AI",
    "🔍 Binary Search": "games.11_binary_search",
    "💣 Minesweeper": "games.12_minesweeper",
    "🧩 Sudoku Solver": "games.13_sudoku_solver",
    "🖼️ Photo Manipulation in Python": "games.14_photo_manipulation_python",
    "📝 Markov Chain Text Composer": "games.15_markov_chain_text_composer",
    "🎮 Pong": "games.16_pong",
    "🐍 Snake": "games.17_snake",
    "🔴 Connect Four": "games.18_connect_four",
    "🧩 Tetris": "games.19_tetris",
    "🌍 Online Multiplayer Game": "games.20_online_multiplayer_game",
    "🌐 Web Scraping Program": "games.21_web_scraping_program",
    "📂 Bulk File Renamer": "games.22_bulk_file_renamer",
    "🌦️ Weather Program": "games.23_weather_program",
    "💬 Code a Discord Bot with Python": "games.24_discord_bot",
    "🚀 Space Invaders Game": "games.25_space_invaders",
}

# --- Sidebar ---
st.sidebar.title("🎮 Game Arcade")
st.sidebar.markdown("### Select a game to play:")

# Home button
if st.sidebar.button("🏠 Home"):
    st.session_state.selected_game = None

# Game buttons
for name, module in games.items():
    if st.sidebar.button(name):
        st.session_state.selected_game = module
        st.rerun()

# --- Main Content ---
selected = st.session_state.get("selected_game")

if not selected:
    st.title("🎉 Welcome to the Python Mini Game Arcade")
    st.markdown("""
        #### How to Play:
        - Use the **sidebar** to choose a game.
        - Each game is built in Python using Streamlit.
        - No installation needed — just click and play!

        ---
        ✅ Perfect for beginners and fun for all!

        👈 Choose a game from the left sidebar to begin.
    """)
else:
    try:
        game_module = importlib.import_module(selected)
        game_module.run()
    except Exception as e:
        st.error(f"Failed to load game: {e}")
