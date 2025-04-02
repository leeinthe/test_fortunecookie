import streamlit as st
import pandas as pd
import random
messages = pd.read_csv("./data/study.csv")


st.title("🎈 포춘쿠키 하나먹어봐요 ")
st.success("지친 여러분을 위해 준비했어요")

st.subheader("포춘쿠키 열어보기")
open_cookie = st.button("포춘쿠키 확인하기")
if open_cookie:
    fortune = random.choice(messages.messages)
    st.warning(fortune)





