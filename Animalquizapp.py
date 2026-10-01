import streamlit as st
import random

st.set_page_config(
    page_title="เกมทายชื่อสัตว์",
    page_icon="🐾",
    layout="centered"
)

# -----------------------------
# ข้อมูลสัตว์ 6 ข้อ
# -----------------------------
animals = [
    {"name": "สุนัข", "emoji": "🐶"},
    {"name": "แมว", "emoji": "🐱"},
    {"name": "ช้าง", "emoji": "🐘"},
    {"name": "สิงโต", "emoji": "🦁"},
    {"name": "แพนด้า", "emoji": "🐼"},
    {"name": "เสือ", "emoji": "🐯"}
]

# -----------------------------
# ตั้งค่าเริ่มต้น
# -----------------------------
if "question" not in st.session_state:
    st.session_state.question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "result" not in st.session_state:
    st.session_state.result = ""


# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #666;
}

.animal {
    text-align: center;
    font-size: 150px;
    background-color: #f5f5f5;
    border-radius: 20px;
    padding: 30px;
    margin: 20px 0;
}

.score {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# หน้าจบเกม
# -----------------------------
if st.session_state.question >= len(animals):

    st.markdown(
        '<div class="main-title">🎉 จบเกม!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="subtitle">คุณได้ {st.session_state.score} / 6 คะแนน</div>',
        unsafe_allow_html=True
    )

    if st.session_state.score == 6:
        st.success("🏆 ยอดเยี่ยม! ตอบถูกทุกข้อ")
    elif st.session_state.score >= 4:
        st.success("👏 เก่งมาก!")
    elif st.session_state.score >= 2:
        st.info("👍 พยายามได้ดี!")
    else:
        st.warning("💪 ลองเล่นอีกครั้งนะ!")

    if st.button("🔄 เล่นอีกครั้ง", use_container_width=True):

        st.session_state.question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.result = ""

        st.rerun()

    st.stop()


# -----------------------------
# แสดงหัวเกม
# -----------------------------
st.markdown(
    '<div class="main-title">🐾 เกมทายชื่อสัตว์ 🐾</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ทายชื่อสัตว์จากภาพให้ครบทั้ง 6 ข้อ</div>',
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    f'<div class="score">ข้อที่ '
    f'{st.session_state.question + 1} / 6 '
    f'| คะแนน: {st.session_state.score}</div>',
    unsafe_allow_html=True
)


# -----------------------------
# สัตว์ปัจจุบัน
# -----------------------------
animal = animals[st.session_state.question]

st.markdown(
    f'<div class="animal">{animal["emoji"]}</div>',
    unsafe_allow_html=True
)

st.subheader("
