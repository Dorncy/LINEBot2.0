county_and_city = ["苗栗", "彰化", "南投", "雲林", "屏東", "台東", "臺東", "花蓮", "宜蘭",
                   "台中", "臺中", "台北", "臺北", "新北", "基隆", "桃園", "高雄", "台南", "臺南", "新竹"]


def search_county(usertext):
    for keyword in county_and_city:
        if keyword in usertext:
            return keyword
