import openai

a_side = 'sk-kLlaxEKQdu0vosdw47OIT3'
b_side = 'BlbkFJsyCfivO94nFMXARHMBhi'
openai.api_key = a_side + b_side

def chat_reply(msg):
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.5,
        messages=[
            {"role": "assistant", "content": "我是負責處理旅遊問題的AI，我會簡短回答你所問的問題。"},
            {"role": "user", "content":  msg}
        ]
    )
    remsg = response.choices[0].message.content
    
    if '。' or '.' in remsg:
        remsg = remsg.split('。')[0]
        
    print(remsg)
    
    return remsg


# chat_reply("台灣哪裡有熱氣球可以搭")

