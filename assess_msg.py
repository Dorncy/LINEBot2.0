import re
from weather import get_weather_data
from get_help import get_help
from search_coutny import search_county
from firebase_read import random_view_introduction, get_all_view
from chatGPT import reply, reply_stablemsg, reply_recommed


def assess(usertext):

    # 天氣
    weather = re.compile('天氣')
    # 幫助
    need_help = re.compile('help')
    # 旅遊, 介紹景點
    travel_1 = re.compile('旅遊')
    travel_2 = re.compile('景點')
    travel_3 = re.compile('推薦')
    # introduction_keyword = ['想了解', '介紹']

    # 天氣
    if re.search(weather, usertext):
        # print(get_weather_data(search_county(usertext)))
        return get_weather_data(search_county(usertext))
    # 操作
    elif re.search(need_help, usertext):
        return get_help()
    # 景點推薦
    elif re.search(travel_3, usertext):
        return reply_recommed(get_all_view(search_county(usertext)))
    elif re.search(travel_1, usertext) or re.search(travel_2, usertext):
        return reply_stablemsg(random_view_introduction(search_county(usertext)))
    else:
        return reply(usertext)


# print(assess(input()))
