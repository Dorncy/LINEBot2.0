# from flask import Flask, render_template, request, make_response, jsonify
# from assess_msg import assess

# # 載入 json 標準函式庫，處理回傳的資料格式
# import json

# # 載入 LINE Message API 相關函式庫
# from linebot import LineBotApi, WebhookHandler
# from linebot.exceptions import InvalidSignatureError
# from linebot.models import MessageEvent, TextMessage, TextSendMessage
# from settings import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET

# app = Flask(__name__)


# @app.route("/", methods=["POST"])
# def linebot():
#     usertext = request.get_data(as_text=True)                    # 取得收到的訊息內容
#     try:
#         json_data = json.loads(usertext)                         # json 格式化訊息內容
#         access_token = LINE_CHANNEL_ACCESS_TOKEN
#         secret = LINE_CHANNEL_SECRET
#         # 確認 token 是否正確
#         line_bot_api = LineBotApi(access_token)
#         # 確認 secret 是否正確
#         handler = WebhookHandler(secret)
#         # 加入回傳的 headers
#         signature = request.headers['X-Line-Signature']
#         handler.handle(usertext, signature)                      # 綁定訊息回傳的相關資訊
#         # 取得回傳訊息的 Token
#         tk = json_data['events'][0]['replyToken']
#         # 取得 LINe 收到的訊息類型
#         type = json_data['events'][0]['message']['type']

# #   --------------------------------------------------------------------------------------------#

#         if type == 'text':                                       # 主要回覆問答

#             # 取得 LINE 收到的文字訊息
#             msg = json_data['events'][0]['message']['text']
#             # print(msg)                                           # 印出內容
#             reply = assess(msg)
#         else:
#             reply = '你傳的不是文字呦～'
#         # print(reply)
#         line_bot_api.reply_message(tk, TextSendMessage(reply))   # 回傳訊息
#     except:
#         # 如果發生錯誤，印出收到的內容
#         print(usertext)
#     return 'OK'                                                  # 驗證 Webhook 使用，不能省略


# if __name__ == "__main__":
#     app.run()

from firebase import firebase
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, ImageSendMessage
import json
import requests
from settings import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET

import openai
a_side = "sk-lzgi3gzKfyYD6giZVCuMT3Blb"
b_side = "kFJYmxI29t3g669SYateckI"
openai.api_key = a_side + b_side

url = 'https://chatgpt-data-52e1e-default-rtdb.firebaseio.com'

# 你的 Firebase Realtime database URL
fdb = firebase.FirebaseApplication(url, None)  # 初始化 Firebase Realtime database

app = Flask(__name__)


@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        token = LINE_CHANNEL_ACCESS_TOKEN        # 你的 Access Token
        secret = LINE_CHANNEL_SECRET             # 你的 Channel Secret
        line_bot_api = LineBotApi(token)
        handler = WebhookHandler(secret)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']            # 回覆的 reply token
        timestamp = json_data['events'][0]['timestamp']      # 訊息時間戳
        msg_type = json_data['events'][0]['message']['type']  # 訊息類型
        # 如果是文字訊息
        if msg_type == 'text':
            msg = json_data['events'][0]['message']['text']  # 取出文字內容
            # 讀取 Firebase 資料庫內容
            chatgpt = fdb.get('/', 'chatgpt')

            if chatgpt == None:
                messages = []       # 如果資料庫裡沒有內容，建立空串列
            else:
                messages = chatgpt  # 如果資料庫裡有內容，設定歷史紀錄為資料庫內容

            if msg == '!reset':
                fdb.delete('/', 'chatgpt')    # 如果收到 !reset 的訊息，表示清空資料庫內容
                reply_msg = TextSendMessage(text='對話歷史紀錄已經清空！')
            else:
                # 如果是一般文字訊息，將訊息添加到歷史紀錄裡
                messages.append({"role": "user", "content": msg})
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    max_tokens=128,
                    temperature=0.5,
                    messages=messages
                )
                ai_msg = response.choices[0].message.content.replace(
                    '\n', '')  # 移除回應裡的換行符
                # 歷史紀錄裡添加回應訊息
                messages.append({"role": "assistant", "content": ai_msg})
                fdb.put_async('/', 'chatgpt', messages)        # 使用非同步的方式紀錄訊息
                reply_msg = TextSendMessage(text=ai_msg)     # 回應訊息
            line_bot_api.reply_message(tk, reply_msg)
        else:
            reply_msg = TextSendMessage(text='你傳的不是文字訊息呦')
            line_bot_api.reply_message(tk, reply_msg)
    except:
        print('error')
    return 'OK'


if __name__ == "__main__":
    app.run()
