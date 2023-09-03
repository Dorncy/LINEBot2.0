import openai
import os

a_side = "sk-lzgi3gzKfyYD6giZVCuMT3Blb"
b_side = "kFJYmxI29t3g669SYateckI"
openai.api_key = os.getenv("OPENAI_API_KEY")


def reply(msg):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=700,
        temperature=0.3,
        messages=[
            {"role": "assistant", "content": "我會盡量以繁體中文和口頭聊天的方式回覆"},
            {"role": "user", "content":  msg}
        ]
    )
    remsg = response.choices[0].message.content

    # if '。' or '.' in remsg:
    #     remsg = remsg.split('。')[0]

    # print(remsg)

    return remsg


# reply("台灣哪裡有熱氣球可以搭")
