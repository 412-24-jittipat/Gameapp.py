import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="เกมทายชื่อสัตว์",
    page_icon="🐾",
    layout="centered"
)

# -------------------------
# CSS ตกแต่งเว็บไซต์
# -------------------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #333333;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #666666;
}

.animal-box {
    background-color: #eeeeee;
    border-radius: 25px;
    padding: 30px;
    text-align: center;
    margin: 20px 0;
}

.animal-emoji {
    font-size: 150px;
}

.score {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

.result {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# -------------------------
# ข้อมูลสัตว์ 6 ตัว
# -------------------------
animals = [
    {
        "name": "สุนัข",
        "image": "🐶"
    },
    {
        "name": "แมว",
        "image": "🐱"
    },
    {
        "name": "ช้าง",
        "image": "🐘"
    },
    {
        "name": "สิงโต",
        "image": "🦁"
    },
    {
        "name": "แพนด้า",
        "image": "🐼"
    },
    {
        "name": "เสือ",
        "image": "🐯"
    }
]


# -------------------------
# ตัวแปรของเกม
# -------------------------
if "question" not in st.session_state:
    st.session_state.question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "result" not in st.session_state:
    st.session_state.result = ""


# -------------------------
# ตรวจว่าจบเกมหรือยัง
# -------------------------
if st.session_state.question >= 6:

    st.markdown(
        '<div class="title">🎉 จบเกมแล้ว!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="subtitle">'
        f'คุณได้คะแนน {st.session_state.score} / 6'
        f'</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.session_state.score == 6:
        st.success("🏆 ยอดเยี่ยม! ตอบถูกครบทุกข้อ")

    elif st.session_state.score >= 4:
        st.success("👏 เก่งมาก!")

    elif st.session_state.score >= 2:
        st.info("👍 ทำได้ดี ลองเล่นอีกครั้งเพื่อทำคะแนนเพิ่ม")

    else:
        st.warning("💪 ลองเล่นใหม่อีกครั้งนะ")


    if st.button(
        "🔄 เล่นอีกครั้ง",
        use_container_width=True
    ):

        st.session_state.question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.result = ""

        st.rerun()

    st.stop()


# -------------------------
# หัวข้อเกม
# -------------------------
st.markdown(
    '<div class="title">🐾 เกมทายชื่อสัตว์ 🐾</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'ทายชื่อสัตว์จากภาพทั้งหมด 6 ข้อ'
    '</div>',
    unsafe_allow_html=True
)

st.write("")


# -------------------------
# คะแนน
# -------------------------
st.markdown(
    f'<div class="score">'
    f'ข้อที่ {st.session_state.question + 1} / 6'
    f'　|　คะแนน {st.session_state.score}'
    f'</div>',
    unsafe_allow_html=True
)


# -------------------------
# แสดงภาพสัตว์
# -------------------------
animal = animals[st.session_state.question]

st.markdown(
    f"""
    <div class="animal-box">
        <div class="animal-emoji">
            {animal["image"]}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# -------------------------
# คำถาม
# -------------------------
st.subheader("❓ สัตว์ในภาพคืออะไร?")


# -------------------------
# ช่องกรอกคำตอบ
# -------------------------
answer = st.text_input(
    "พิมพ์ชื่อสัตว์",
    placeholder="เช่น แมว",
    disabled=st.session_state.answered
)


# -------------------------
# ปุ่มตรวจคำตอบ
# -------------------------
if not st.session_state.answered:

    if st.button(
        "✅ ตรวจคำตอบ",
        use_container_width=True
    ):

        if answer.strip() == "":
            st.warning("⚠️ กรุณาพิมพ์คำตอบก่อน")

        else:

            correct_answer = animal["name"]

            if answer.strip() == correct_answer:

                st.session_state.score += 1

                st.session_state.result = "ถูก"

            else:

                st.session_state.result = (
                    f"ผิด! คำตอบที่ถูกคือ {correct_answer}"
                )

            st.session_state.answered = True

            st.rerun()


# -------------------------
# แสดงผลลัพธ์
# -------------------------
if st.session_state.answered:

    if st.session_state.result == "ถูก":

        st.success("🎉 ถูกต้อง!")

    else:

        st.error(
            "❌ " + st.session_state.result
        )


    # -------------------------
    # ปุ่มข้อถัดไป
    # -------------------------
    if st.button(
        "➡️ ข้อถัดไป",
        use_container_width=True
    ):

        st.session_state.question += 1

        st.session_state.answered = False

        st.session_state.result = ""

        st.rerun()
