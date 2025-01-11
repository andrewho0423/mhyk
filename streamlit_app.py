import streamlit as st
from PIL import Image
from calculate import percentage_calculate

image = Image.open("favicon.ico")
st.set_page_config(
    page_title="法使小人計算機",
    page_icon=image,
    # layout="wide",
)
st.title("魔法使的約定--活動覺醒小人特效%數計算機")

# Initialize some parameters
type_0, type_1, type_2, type_3, type_4, type_5 = "抽卡", "抽卡", "抽卡", "抽卡", "抽卡", "抽卡"
totsu_0, totsu_1, totsu_2, totsu_3, totsu_4, totsu_5 = 0,0,0,0,0,0

event = st.radio(
    label = "請選擇活動類型",
    options = ["一般活動", "祭典(祝祭)", "奏鳴曲(ソナチネ)"],
    horizontal=True,
    key="event"
)
if event == "祭典(祝祭)":
    kakusei_rarity = st.radio(
        label = "請選擇小人稀有度(若活動選擇祭典，則只有三星小人；若活動選擇奏鳴曲，則只有四星小人)",
        options = ["3星"],
        key="kakusei_rarity"
    )
    main = st.radio(
        label="請選擇故事卡(主卡)的稀有度",
        options=["非活動卡", "SSR", "SR", "R"],
        horizontal=True,
        key="main"
    )
    if main != "非活動卡":
        type_0 = st.radio(
            label="請選擇故事卡(主卡)的獲得方式",
            options=["抽卡", "報酬"],
            horizontal=True,
            key="type_0"
        )
        totsu_0 = st.number_input(
            label="請選擇突破數",
            min_value=0,
            max_value=5,
            value="min",
            key="totsu_0"
        )

    team_1 = st.radio(
        label="請選擇隊員卡1的稀有度與突破數",
        options=["非活動卡", "SSR", "SR", "R"],
        horizontal=True,
        key="team_1"
    )
    if team_1 != "非活動卡":
        type_1 = st.radio(
            label="請選擇隊員卡1的獲得方式",
            options=["抽卡", "報酬"],
            horizontal=True,
            key="type_1"
        )
        totsu_1 = st.number_input(
            label="請選擇突破數",
            min_value=0,
            max_value=5,
            value="min",
            key="totsu_1"
        )
    team_2 = st.radio(
        label="請選擇隊員卡2的稀有度與突破數",
        options=["非活動卡", "SSR", "SR", "R"],
        horizontal=True,
        key="team_2"
    )
    if team_2 != "非活動卡":
        type_2 = st.radio(
            label="請選擇隊員卡2的獲得方式",
            options=["抽卡", "報酬"],
            horizontal=True,
            key="type_2"
        )
        totsu_2 = st.number_input(
            label="請選擇突破數",
            min_value=0,
            max_value=5,
            value="min",
            key="totsu_2"
        )
    team_3 = st.radio(
        label="請選擇隊員卡3的稀有度與突破數",
        options=["非活動卡", "SSR", "SR", "R"],
        horizontal=True,
        key="team_3"
    )
    if team_3 != "非活動卡":
        type_3 = st.radio(
            label="請選擇隊員卡3的獲得方式",
            options=["抽卡", "報酬"],
            horizontal=True,
            key="type_3"
        )
        totsu_3 = st.number_input(
            label="請選擇突破數",
            min_value=0,
            max_value=5,
            value="min",
            key="totsu_3"
        )
    team_4 = st.radio(
        label="請選擇隊員卡3的稀有度與突破數",
        options=["非活動卡", "SSR", "SR", "R"],
        horizontal=True,
        key="team_4"
    )
    if team_4 != "非活動卡":
        type_4 = st.radio(
            label="請選擇隊員卡4的獲得方式",
            options=["抽卡", "報酬"],
            horizontal=True,
            key="type_4"
        )
        totsu_4 = st.number_input(
            label="請選擇突破數",
            min_value=0,
            max_value=5,
            value="min",
            key="totsu_4"
        )
    team_5 = st.radio(
        label="請選擇好友的稀有度與突破數",
        options=["非活動卡", "SSR(自己)", "SR(自己)", "R(自己)", "好友卡(默認SSR)"],
        horizontal=True,
        key="team_5"
    )
    if team_5 not in ["非活動卡", "好友卡(默認SSR)"]:
        type_5 = st.radio(
            label="請選擇好友卡的獲得方式",
            options=["抽卡", "報酬"],
            horizontal=True,
            key="type_5"
        )
        totsu_5 = st.number_input(
            label="請選擇突破數",
            min_value=0,
            max_value=5,
            value="min",
            key="totsu_5"
        )
elif event == "奏鳴曲(ソナチネ)":
    kakusei_rarity = st.radio(
        label = "請選擇小人稀有度(若活動選擇祭典，則只有三星小人；若活動選擇奏鳴曲，則只有四星小人)",
        options = ["4星"],
        key="kakusei_rarity_1"
    )
else:
    kakusei_rarity = st.radio(
        label = "請選擇小人稀有度(若活動選擇祭典，則只有三星小人；若活動選擇奏鳴曲，則只有四星小人)",
        options = ["4星", "3星"],
        key="kakusei_rarity_2"
    )

if event == "祭典(祝祭)":
    if st.button(label="開始計算"):
        percentage = percentage_calculate(
            event=event,
            kakusei_rarity=kakusei_rarity,
            main=main,
            team_1=team_1,
            team_2=team_2,
            team_3=team_3,
            team_4=team_4,
            team_5=team_5,
            type_0=type_0,
            type_1=type_1,
            type_2=type_2,
            type_3=type_3,
            type_4=type_4,
            type_5=type_5,
            totsu_0=totsu_0,
            totsu_1=totsu_1,
            totsu_2=totsu_2,
            totsu_3=totsu_3,
            totsu_4=totsu_4,
            totsu_5=totsu_5,
        )
        st.write("您的活動小人特效%數是: "+str(percentage)+"%")
