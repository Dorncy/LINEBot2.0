import re
from weather import get_weather_data
from get_help import get_help
from search_coutny import search_county
from firebase_read import get_all_view
from chatGPT import reply


def assess(usertext):

    # 天氣
    weather = re.compile('天氣')
    # 幫助
    need_help = re.compile('help')
    # 旅遊
    travel_keyword = ["旅遊", "景點"]
    for keywords in travel_keyword:
        travel = re.compile(keywords)

    if re.search(weather, usertext):
        # print(get_weather_data(search_county(usertext)))
        return get_weather_data(search_county(usertext))
    elif re.search(need_help, usertext):
        return get_help()
    elif re.search(travel, usertext):
        return get_all_view(search_county(usertext))
    else:
        return reply(usertext)


print(assess(input()))
