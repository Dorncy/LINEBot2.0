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
            {"role": "assistant", "content": "我將會推薦你一個你所選地區的景點資料作介紹。"},
            {"role": "assistant", "content": "這是我推薦的景點資料" + msg},
            {"role": "user", "content": "用一句話介紹這個景點，並將「我推薦你」溶入回復句當中。"}
        ]
    )
    remsg = response.choices[0].message.content

    # print(remsg)

    return remsg
