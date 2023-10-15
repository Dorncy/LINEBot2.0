import re
from weather import get_weather_data
from get_help import get_help
from search_coutny import search_county
from firebase_read import get_all_view, random_view_introduction
from chatGPT import reply, reply_stablemsg


def assess(usertext):

    # 天氣
    weather = re.compile('天氣')
    # 幫助
    need_help = re.compile('help')
    # 旅遊, 介紹景點
    travel_keyword = ["旅遊", "景點"]
    # introduction_keyword = ['想了解', '介紹']

    for keywords in travel_keyword:
        travel = re.compile(keywords)

    if re.search(weather, usertext):
        # print(get_weather_data(search_county(usertext)))
        return get_weather_data(search_county(usertext))
    elif re.search(need_help, usertext):
        return get_help()
    elif re.search(travel, usertext):
        return random_view_introduction(search_county(usertext))
    else:
        return reply(usertext)


# print(assess(input()))
