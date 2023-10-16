import openai
import os

a_side = "sk-lzgi3gzKfyYD6giZVCuMT3Blb"
b_side = "kFJYmxI29t3g669SYateckI"
openai.api_key = a_side + b_side


def reply(msg):

    messages = []
    while True:
        messages.append({"role": "user", "content": msg})   # 添加 user 回應
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=64,
            temperature=0.5,
            messages=messages
        )
        ai_msg = response.choices[0].message.content.replace('\n', '')
        return ai_msg


# print(reply("講個笑話"))


def reply_stablemsg(msg):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=128,
        temperature=0.5,
        messages=[
            {"role": "assistant", "content": "我是一個專門介紹台灣各大縣市旅有景點的機器人。"},
            {"role": "assistant",
                "content": "我將會推薦你一個你所選地區的景點資料作介紹，並且以「我推薦你xxxx，'景點介紹'」為回覆方式"},
            {"role": "assistant", "content": "這是我隨機挑選的推薦景點資料" + msg},
            {"role": "user", "content": "回復我你對於景點一句話以內的推薦。"}
        ]
    )
    remsg = response.choices[0].message.content

    # print(remsg)

    return remsg

# recommend


def reply_recommed(msg):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=128,
        temperature=0.5,
        messages=[
            {"role": "assistant", "content": msg},
            {"role": "user", "content": "從以上景點隨機挑選1個景點做推薦，在一句話以內。"}

        ]
    )
    remsg = response.choices[0].message.content

    # print(remsg)

    return remsg


# weather
def reply_weather(msg):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=128,
        temperature=0.5,
        messages=[
            {"role": "assistant", "content": msg},
            {"role": "user", "content": "整理天氣訊息以簡單的口語作為回復。"}

        ]
    )
    remsg = response.choices[0].message.content

    # print(remsg)

    return remsg
