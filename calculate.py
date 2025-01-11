
PERC_DICT = {
    "小人稀有度":
        {
            "3星": 3,
            "4星": 5
        },
    "抽卡": {
        "SSR": 10,
        "SR": 5,
        "R": 2
    },
    "報酬": {
        "SSR": 7,
        "SR": 3,
        "R": 1
    }
}

def percentage_calculate(
    event: str,
    kakusei_rarity: str,
    main: str,
    team_1: str,
    team_2: str,
    team_3: str,
    team_4: str,
    type_0: str="抽卡",
    type_1: str="抽卡",
    type_2: str="抽卡",
    type_3: str="抽卡",
    type_4: str="抽卡",
    totsu_0: int=0,
    totsu_1: int=0,
    totsu_2: int=0,
    totsu_3: int=0,
    totsu_4: int=0,
):
    kakusei_perc = PERC_DICT["小人稀有度"][kakusei_rarity]
    perc_0 = 0 if main == "非活動卡" else PERC_DICT[type_0][main]*totsu_0
    perc_1 = 0 if team_1 == "非活動卡" else PERC_DICT[type_1][team_1]*totsu_1
    perc_2 = 0 if team_2 == "非活動卡" else PERC_DICT[type_2][team_2]*totsu_2
    perc_3 = 0 if team_3 == "非活動卡" else PERC_DICT[type_3][team_3]*totsu_3
    if team_4 == "好友卡(默認SSR)":
        perc_4 = 10
    else:
        perc_4 = 0 if team_4 == "非活動卡" else PERC_DICT[type_4][team_4]*totsu_4
    perc_total = kakusei_perc+min(perc_0+perc_1+perc_2+perc_3+perc_4, 60)
    return perc_total