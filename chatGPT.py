import openai
import os

a_side = "sk-lzgi3gzKfyYD6giZVCuMT3Blb"
b_side = "kFJYmxI29t3g669SYateckI"
openai.api_key = a_side + b_side


def reply(msg):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        max_tokens=350,
        temperature=0.5,
        messages=[
            {"role": "assistant", "content": "將以150字上下來回復所有訊息。"},
            {"role": "user", "content":  msg}
        ]
    )
    remsg = response.choices[0].message.content

    # if '。' or '.' in remsg:
    #     remsg = remsg.split('。')[0]

    # print(remsg)

    return remsg


# print(reply("介紹台中的草悟道"))
