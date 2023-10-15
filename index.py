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
import openai

from flask import Flask, request

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage   # 載入 TextSendMessage 模組
from settings import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET
import json

app = Flask(__name__)


@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
        handler = WebhookHandler(LINE_CHANNEL_SECRET)
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)
        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']
        # 取出文字的前五個字元，轉換成小寫
        ai_msg = msg[:6].lower()
        reply_msg = ''
        # 取出文字的前五個字元是 hi ai:
        if ai_msg == 'hi ai:':
            a_side = "sk-lzgi3gzKfyYD6giZVCuMT3Blb"
            b_side = "kFJYmxI29t3g669SYateckI"
            openai.api_key = a_side + b_side
            # 將第六個字元之後的訊息發送給 OpenAI
            response = openai.Completion.create(
                model='text-davinci-003',
                prompt=msg[6:],
                max_tokens=256,
                temperature=0.5,
            )
            # 接收到回覆訊息後，移除換行符號
            reply_msg = response["choices"][0]["text"].replace('\n', '')
        else:
            reply_msg = msg
        text_message = TextSendMessage(text=reply_msg)
        line_bot_api.reply_message(tk, text_message)
    except:
        print('error')
    return 'OK'


if __name__ == "__main__":
    app.run()
