import streamlit as st
import random

# Set Streamlit Page Config
st.set_page_config(
    page_title="🏏 Hand Cricket",
    page_icon="🏏",
    layout="centered"
)

# Custom CSS for Modern Scoreboard UI
st.markdown("""
<style>
    /* Global Container & Spacing */
    .main .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2.5rem;
        max-width: 750px;
    }
    
    /* Header Card */
    .game-header {
        text-align: center;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        color: #f8fafc;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
        margin-bottom: 20px;
        border: 1px solid #334155;
    }
    .game-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.5px;
        color: #f8fafc;
    }
    .game-subtitle {
        font-size: 1.05rem;
        color: #94a3b8;
        margin-top: 4px;
        font-weight: 500;
    }
    
    /* Status Bar */
    .status-badge-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-bottom: 16px;
    }
    .status-pill {
        background: #1e293b;
        color: #e2e8f0;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1px solid #475569;
    }
    .status-pill.highlight {
        background: #0284c7;
        color: #ffffff;
        border-color: #38bdf8;
    }

    /* Scoreboard */
    .scoreboard-grid {
        display: flex;
        justify-content: space-around;
        gap: 16px;
        margin-bottom: 20px;
    }
    .score-card {
        flex: 1;
        background: #1e293b;
        color: #f8fafc;
        border-radius: 14px;
        padding: 16px;
        text-align: center;
        border: 2px solid #334155;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    .score-card.active-batting {
        border-color: #22c55e;
        box-shadow: 0 0 16px rgba(34, 197, 94, 0.25);
    }
    .score-card.active-bowling {
        border-color: #eab308;
        box-shadow: 0 0 16px rgba(234, 179, 8, 0.25);
    }
    .score-title {
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #94a3b8;
        margin-bottom: 6px;
        font-weight: 700;
    }
    .score-value {
        font-size: 2.6rem;
        font-weight: 800;
        color: #38bdf8;
        line-height: 1.1;
    }
    .role-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: 700;
        margin-top: 8px;
        text-transform: uppercase;
    }
    .badge-bat {
        background-color: #14532d;
        color: #4ade80;
        border: 1px solid #22c55e;
    }
    .badge-bowl {
        background-color: #713f12;
        color: #fde047;
        border: 1px solid #eab308;
    }

    /* Target Box */
    .target-banner {
        background: linear-gradient(90deg, #312e81 0%, #1e1b4b 100%);
        color: #e0e7ff;
        border-radius: 10px;
        padding: 10px 16px;
        text-align: center;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 20px;
        border: 1px solid #4338ca;
    }

    /* Turn Result Box */
    .turn-box {
        background: #0f172a;
        color: #f8fafc;
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #334155;
    }
    .turn-numbers {
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .out-text {
        color: #ef4444;
        font-weight: 800;
        font-size: 1.2rem;
    }
    .score-text {
        color: #38bdf8;
        font-weight: 600;
    }

    /* Centered Button Grid Helper */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 700;
        padding: 10px 0px;
        transition: all 0.2s ease-in-out;
    }
</style>
""", unsafe_allow_html=True)


# Initialize Session State
def init_game_state():
    if "game_stage" not in st.session_state:
        st.session_state.game_stage = "toss"
    if "toss1" not in st.session_state:
        st.session_state.toss1 = "heads"
    if "toss" not in st.session_state:
        st.session_state.toss = None
    if "toss_winner" not in st.session_state:
        st.session_state.toss_winner = None
    if "choicep" not in st.session_state:
        st.session_state.choicep = ""
    if "choiceb" not in st.session_state:
        st.session_state.choiceb = ""
    if "score_player" not in st.session_state:
        st.session_state.score_player = 0
    if "score_bot" not in st.session_state:
        st.session_state.score_bot = 0
    if "flag" not in st.session_state:
        st.session_state.flag = 1
    if "current_innings" not in st.session_state:
        st.session_state.current_innings = 1
    if "last_turn" not in st.session_state:
        st.session_state.last_turn = None
    if "innings_msg" not in st.session_state:
        st.session_state.innings_msg = ""


def reset_game():
    st.session_state.game_stage = "toss"
    st.session_state.toss1 = "heads"
    st.session_state.toss = None
    st.session_state.toss_winner = None
    st.session_state.choicep = ""
    st.session_state.choiceb = ""
    st.session_state.score_player = 0
    st.session_state.score_bot = 0
    st.session_state.flag = 1
    st.session_state.current_innings = 1
    st.session_state.last_turn = None
    st.session_state.innings_msg = ""


init_game_state()

# App Header
st.markdown("""
<div class="game-header">
    <div class="game-title">🏏 Hand Cricket</div>
    <div class="game-subtitle">Player vs Bot</div>
</div>
""", unsafe_allow_html=True)


# --- STAGE 1: TOSS SCREEN ---
if st.session_state.game_stage == "toss":
    st.subheader("🪙 Toss")
    
    toss_choice = st.radio(
        "Choose heads or tails:",
        options=["heads", "tails"],
        horizontal=True,
        index=0 if st.session_state.toss1 == "heads" else 1,
        key="toss_radio"
    )
    st.session_state.toss1 = toss_choice

    if st.button("Flip Coin & Toss", type="primary", use_container_width=True):
        opt = ["heads", "tails"]
        toss_result = random.choice(opt)
        st.session_state.toss = toss_result

        if toss_result == st.session_state.toss1:
            st.session_state.toss_winner = "player"
            st.session_state.game_stage = "toss_choice"
        else:
            st.session_state.toss_winner = "bot"
            choiceb = random.choice(["bat", "bowl"])
            st.session_state.choiceb = choiceb
            st.session_state.choicep = ""
            st.session_state.game_stage = "playing"
            st.session_state.current_innings = 1
            st.session_state.innings_msg = f"You lost the toss and opponent chose {choiceb.upper()}."
        st.rerun()


# --- STAGE 1b: PLAYER TOSS WIN CHOICE ---
elif st.session_state.game_stage == "toss_choice":
    st.success(f"🪙 Coin result: **{st.session_state.toss.upper()}**!")
    st.info("Congratulations! You won the toss!")
    st.write("### Choose bat or bowl:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏏 Bat", type="primary", use_container_width=True):
            st.session_state.choicep = "bat"
            st.session_state.choiceb = ""
            st.session_state.game_stage = "playing"
            st.session_state.current_innings = 1
            st.session_state.innings_msg = "You won the toss and chose to BAT first."
            st.rerun()
    with col2:
        if st.button("⚾ Bowl", type="secondary", use_container_width=True):
            st.session_state.choicep = "bowl"
            st.session_state.choiceb = ""
            st.session_state.game_stage = "playing"
            st.session_state.current_innings = 1
            st.session_state.innings_msg = "You won the toss and chose to BOWL first."
            st.rerun()


# --- STAGE 2: PLAYING SCREEN ---
elif st.session_state.game_stage == "playing":
    player_bats_first = (st.session_state.choicep == "bat" or st.session_state.choiceb == "bowl")

    # Current role badges
    if st.session_state.current_innings == 1:
        player_role = "BAT" if player_bats_first else "BOWL"
        bot_role = "BOWL" if player_bats_first else "BAT"
    else:
        player_role = "BOWL" if player_bats_first else "BAT"
        bot_role = "BAT" if player_bats_first else "BOWL"

    # Status Pills
    st.markdown(f"""
    <div class="status-badge-container">
        <div class="status-pill highlight">Innings {st.session_state.current_innings} of 2</div>
        <div class="status-pill">{st.session_state.innings_msg}</div>
    </div>
    """, unsafe_allow_html=True)

    # Target banner for Innings 2
    if st.session_state.current_innings == 2:
        if player_bats_first:
            # Bot is chasing player's score
            target = st.session_state.score_player + 1
            st.markdown(f"""
            <div class="target-banner">
                🎯 Bot needs {target - st.session_state.score_bot} runs to win (Target: {target})
            </div>
            """, unsafe_allow_html=True)
        else:
            # Player is chasing bot's score
            target = st.session_state.score_bot + 1
            st.markdown(f"""
            <div class="target-banner">
                🎯 Player needs {target - st.session_state.score_player} runs to win (Target: {target})
            </div>
            """, unsafe_allow_html=True)

    # Scoreboard
    p_card_class = "active-batting" if player_role == "BAT" else "active-bowling"
    b_card_class = "active-batting" if bot_role == "BAT" else "active-bowling"
    
    p_badge_class = "badge-bat" if player_role == "BAT" else "badge-bowl"
    b_badge_class = "badge-bat" if bot_role == "BAT" else "badge-bowl"

    st.markdown(f"""
    <div class="scoreboard-grid">
        <div class="score-card {p_card_class}">
            <div class="score-title">👤 Player</div>
            <div class="score-value">{st.session_state.score_player}</div>
            <div class="role-badge {p_badge_class}">{player_role}</div>
        </div>
        <div class="score-card {b_card_class}">
            <div class="score-title">🤖 Bot</div>
            <div class="score-value">{st.session_state.score_bot}</div>
            <div class="role-badge {b_badge_class}">{bot_role}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Last Turn Summary
    if st.session_state.last_turn:
        turn = st.session_state.last_turn
        is_out = turn["is_out"]
        status_html = f'<div class="out-text">⚡ OUT!</div>' if is_out else f'<div class="score-text">{turn["msg"]}</div>'
        st.markdown(f"""
        <div class="turn-box">
            <div class="turn-numbers">👤 You: <b>{turn["player"]}</b> &nbsp;|&nbsp; 🤖 Bot: <b>{turn["bot"]}</b></div>
            {status_html}
        </div>
        """, unsafe_allow_html=True)

    st.write("### Choose your number (1-10):")

    # Turn Execution Function exactly matching original Python loops & conditions
    def make_move(choice1):
        choice2 = random.randint(1, 10)
        p_bats_1st = (st.session_state.choicep == "bat" or st.session_state.choiceb == "bowl")

        if p_bats_1st:
            # --- Case 1: Player bats 1st ---
            if st.session_state.current_innings == 1:
                # 1st Innings: Player bats
                if choice1 == choice2:
                    st.session_state.last_turn = {
                        "player": choice1, "bot": choice2, "is_out": True,
                        "msg": f"You got out! Final score: {st.session_state.score_player}"
                    }
                    st.session_state.current_innings = 2
                    st.session_state.innings_msg = f"1st Innings Over. Bot needs {st.session_state.score_player + 1} runs."
                else:
                    st.session_state.score_player += choice1
                    st.session_state.last_turn = {
                        "player": choice1, "bot": choice2, "is_out": False,
                        "msg": f"+{choice1} runs scored! Score: {st.session_state.score_player}"
                    }
            else:
                # 2nd Innings: Bot bats (Original condition: while score_player >= score_bot:)
                if choice1 == choice2:
                    st.session_state.last_turn = {
                        "player": choice1, "bot": choice2, "is_out": True,
                        "msg": f"Bot got out! Final bot score: {st.session_state.score_bot}"
                    }
                    st.session_state.flag = 1
                    st.session_state.game_stage = "game_over"
                else:
                    st.session_state.score_bot += choice2
                    st.session_state.flag = 0
                    st.session_state.last_turn = {
                        "player": choice1, "bot": choice2, "is_out": False,
                        "msg": f"Bot scored +{choice2} runs! Bot Score: {st.session_state.score_bot}"
                    }
                    # Check loop exit condition: score_player >= score_bot fails when score_bot > score_player
                    if st.session_state.score_bot > st.session_state.score_player:
                        st.session_state.game_stage = "game_over"
        else:
            # --- Case 2: Bot bats 1st ---
            if st.session_state.current_innings == 1:
                # 1st Innings: Bot bats
                if choice1 == choice2:
                    st.session_state.last_turn = {
                        "player": choice1, "bot": choice2, "is_out": True,
                        "msg": f"Bot got out! Final bot score: {st.session_state.score_bot}"
                    }
                    st.session_state.current_innings = 2
                    st.session_state.innings_msg = f"1st Innings Over. You need {st.session_state.score_bot + 1} runs."
                else:
                    st.session_state.score_bot += choice2
                    st.session_state.last_turn = {
                        "player": choice1, "bot": choice2, "is_out": False,
                        "msg": f"Bot scored +{choice2} runs! Score: {st.session_state.score_bot}"
                    }
            else:
                # 2nd Innings: Player bats (Original condition: while score_player <= score_bot:)
                if choice1 == choice2:
                    st.session_state.last_turn = {
                        "player": choice1, "bot": choice2, "is_out": True,
                        "msg": f"Player got out! Final score: {st.session_state.score_player}"
                    }
                    st.session_state.flag = 0
                    st.session_state.game_stage = "game_over"
                else:
                    st.session_state.score_player += choice1
                    st.session_state.flag = 1
                    st.session_state.last_turn = {
                        "player": choice1, "bot": choice2, "is_out": False,
                        "msg": f"+{choice1} runs scored! Player Score: {st.session_state.score_player}"
                    }
                    # Check loop exit condition: score_player <= score_bot fails when score_player > score_bot
                    if st.session_state.score_player > st.session_state.score_bot:
                        st.session_state.game_stage = "game_over"

    # Number Buttons 1 to 10 in two 5-column rows
    row1_cols = st.columns(5)
    for i in range(1, 6):
        with row1_cols[i - 1]:
            if st.button(f"{i}", key=f"btn_{i}", use_container_width=True):
                make_move(i)
                st.rerun()

    row2_cols = st.columns(5)
    for i in range(6, 11):
        with row2_cols[i - 6]:
            if st.button(f"{i}", key=f"btn_{i}", use_container_width=True):
                make_move(i)
                st.rerun()


# --- STAGE 3: GAME OVER SCREEN ---
elif st.session_state.game_stage == "game_over":
    st.subheader("🏁 Match Summary")

    # Scoreboard Summary
    st.markdown(f"""
    <div class="scoreboard-grid">
        <div class="score-card">
            <div class="score-title">👤 Final Player Score</div>
            <div class="score-value">{st.session_state.score_player}</div>
        </div>
        <div class="score-card">
            <div class="score-title">🤖 Final Bot Score</div>
            <div class="score-value">{st.session_state.score_bot}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Result Evaluation strictly matching original Python code:
    # if score_player == score_bot: print("Match got tie")
    # elif flag == 1: print("Congratulations u won!!")
    # else: print("Better luck next time")
    if st.session_state.score_player == st.session_state.score_bot:
        st.info("🤝 Match got tie")
    elif st.session_state.flag == 1:
        st.success("🎉 Congratulations u won!!")
    else:
        st.error("💔 Better luck next time")

    st.write("---")

    if st.button("🔄 Play Again", type="primary", use_container_width=True):
        reset_game()
        st.rerun()
