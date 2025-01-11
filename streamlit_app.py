import streamlit as st

st.title("魔法使的約定--活動覺醒小人特效%數計算機")

event = st.radio(
    label = "請選擇活動類型",
    options = ["一般活動", "祭典(祝祭)", "奏鳴曲(ソナチネ)"]
)
