import streamlit as st
from kerykeion import AstrologicalSubject
from datetime import datetime

st.set_page_config(page_title="ホロスコープ相談チャット", layout="centered")
st.title("🔮 ホロスコープ相談チャット")

st.markdown("こんにちは。こちらは性格・恋愛・相性・未来予測をお伝えするホロスコープ診断チャットです。")

# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_input = st.chat_input("生年月日・出生時間・出生地などを入力してください")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        # 例: 1996-5-12 7:00 Tokyo
        parts = user_input.strip().split()
        birth_date = [int(x) for x in parts[0].split("-")]
        birth_time = [int(x) for x in parts[1].split(":")]
        city = parts[2]
        country = parts[3] if len(parts) > 3 else "JP"

        subj = AstrologicalSubject(
            "相談者", birth_date[0], birth_date[1], birth_date[2],
            birth_time[0], birth_time[1], city, country
        )
        chart = subj.chart
        sun = chart.planets["Sun"].sign
        moon = chart.planets["Moon"].sign
        asc = chart.houses["Ascendant"].sign

        response = f"🌞 太陽星座（本質）：{sun}\n🌙 月星座（感情）：{moon}\n🔼 アセンダント（印象）：{asc}\n\nあなたは現実的で安定志向があり、感受性も豊かです。周囲には柔らかく安心感のある印象を与えます。"
    except Exception as e:
        response = f"⚠️ 入力の形式を確認してください（例：1996-5-12 7:00 Tokyo）\nエラー: {e}"

    st.session_state.messages.append({"role": "assistant", "content": response})

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
