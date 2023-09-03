from flask import Flask, render_template, request, make_response, jsonify
import assess_msg

# 載入 json 標準函式庫，處理回傳的資料格式
import json

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from settings import LINE_CHANNEL_ACCESS_TOKEN, LINE_CHANNEL_SECRET

app = Flask(__name__)


@app.route("/", methods=["POST"])
def linebot():
    usertext = request.get_data(as_text=True)                    # 取得收到的訊息內容
    try:
        json_data = json.loads(usertext)                         # json 格式化訊息內容
        access_token = LINE_CHANNEL_ACCESS_TOKEN
        secret = LINE_CHANNEL_SECRET
        # 確認 token 是否正確
        line_bot_api = LineBotApi(access_token)
        # 確認 secret 是否正確
        handler = WebhookHandler(secret)
        # 加入回傳的 headers
        signature = request.headers['X-Line-Signature']
        handler.handle(usertext, signature)                      # 綁定訊息回傳的相關資訊
        # 取得回傳訊息的 Token
        tk = json_data['events'][0]['replyToken']
        # 取得 LINe 收到的訊息類型
        type = json_data['events'][0]['message']['type']

#   --------------------------------------------------------------------------------------------#

        if type == 'text':                                       # 主要回覆問答

            # 取得 LINE 收到的文字訊息
            msg = json_data['events'][0]['message']['text']
            print(msg)                                           # 印出內容
            reply = assess_msg(msg)
        else:
            reply = '你傳的不是文字呦～'
        # print(reply)
        line_bot_api.reply_message(tk, TextSendMessage(reply))   # 回傳訊息
    except:
        # 如果發生錯誤，印出收到的內容
        print(usertext)
    return 'OK'                                                  # 驗證 Webhook 使用，不能省略


if __name__ == "__main__":
    app.run()
