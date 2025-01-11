import streamlit as st

st.title("魔法使的約定--活動覺醒小人特效%數計算機")

event = st.radio(
    label = "請選擇活動類型",
    options = ["一般活動", "祭典(祝祭)", "奏鳴曲(ソナチネ)"],
    horizontal=True
)
if event == "祭典(祝祭)":
    kakusei_rarity = st.radio(
        label = "請選擇小人稀有度(若活動選擇祭典，則只有三星小人；若活動選擇奏鳴曲，則只有四星小人)",
        options = ["3星"]
    )
elif event == "奏鳴曲(ソナチネ)":
    kakusei_rarity = st.radio(
        label = "請選擇小人稀有度(若活動選擇祭典，則只有三星小人；若活動選擇奏鳴曲，則只有四星小人)",
        options = ["4星"]
    )
else:
    kakusei_rarity = st.radio(
        label = "請選擇小人稀有度(若活動選擇祭典，則只有三星小人；若活動選擇奏鳴曲，則只有四星小人)",
        options = ["4星", "3星"]
    )
