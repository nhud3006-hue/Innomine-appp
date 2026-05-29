import streamlit as st
from groq import Groq

st.title("🤖 InnoMine")

# Lấy API Key từ Secrets trên Streamlit
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

nhat_ky = st.text_area("Hôm nay em làm gì?")
cam_xuc = st.text_input("Cảm xúc của em hôm nay?")

if st.button("Lưu & Phân tích"):
    if nhat_ky and cam_xuc:
        with st.spinner("Robot đang phân tích..."):
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Nhật ký: {nhat_ky}. Cảm xúc: {cam_xuc}. Hãy cho lời khuyên."}],
                model="llama3-8b-8192",
            )
            st.success(chat_completion.choices[0].message.content)
    else:
        st.warning("Vui lòng nhập đầy đủ thông tin!")
