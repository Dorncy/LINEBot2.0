import re
from weather import get_weather_data, search_county
from get_help import get_help
from chatGPT import chat_reply

def assess_msg(usertext):

    weather = re.compile('天氣')
    need_help = re.compile('help')

    if re.search(weather, usertext):
        # print(get_weather_data(search_county(usertext)))
        return get_weather_data(search_county(usertext))
    elif re.search(need_help, usertext):
        return get_help()
    else:
        return chat_reply(usertext)

print(assess_msg(input()))