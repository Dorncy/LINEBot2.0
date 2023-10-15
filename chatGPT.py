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
        max_tokens=64,
        temperature=0.5,
        messages=[
            {"role": "user", "content": "推荐個景點"},
            {"role": "assistant", "content": msg},
            {"role": "user", "content": "簡短的用一句話介紹這個景點"}
        ]
    )
    remsg = response.choices[0].message.content

    # print(remsg)

    return remsg
