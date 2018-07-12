from flask import Flask, request
import json
import requests

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

global LINE_API_KEY
global mydict
mydict = {}
LINE_API_KEY = 'Bearer zbzJP1V5BiTWGBUzUAwSo+139oJZ7LUuHdD2AMP4NMTXl7H37EExGqi6l3ciIs51ESQMGCkmq17KIy/MbSbjhD0abjEAjs4+RlZ3iT7bJlT9qTklgrL5QgXzDn+j5YUj3d6PzMn8ngRHB4ibYf1RpQdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)
 
line_bot_api = LineBotApi('zbzJP1V5BiTWGBUzUAwSo+139oJZ7LUuHdD2AMP4NMTXl7H37EExGqi6l3ciIs51ESQMGCkmq17KIy/MbSbjhD0abjEAjs4+RlZ3iT7bJlT9qTklgrL5QgXzDn+j5YUj3d6PzMn8ngRHB4ibYf1RpQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c6d40237131458c24f391675e4d8968a')

@app.route('/')
def index():
    return 'This is chatbot server.'

@app.route('/bot', methods=['POST'])

def bot():
    replyStack = list()
   
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    
    messageType = msg_in_json["events"][0]["message"]["type"]
    if messageType == "text":
        echo = msg_in_json["events"][0]["message"]["text"]
    elif messageType == "sticker":
        packageId = msg_in_json["events"][0]["message"]["packageId"]
        stickerId = msg_in_json["events"][0]["message"]["stickerId"]
        echo = (packageId, stickerId)
    elif messageType == "location":
        title = "Your Location"
        address = msg_in_json["events"][0]["message"]["address"]
        latitude = msg_in_json["events"][0]["message"]["latitude"]
        longitude = msg_in_json["events"][0]["message"]["longitude"]
        echo = (title, address, latitude, longitude)
    else:
        echo = msg_in_string

    replyToken = msg_in_json["events"][0]['replyToken']

    #sourceType = msg_in_json["events"][0]["source"]["type"]
    #userId = msg_in_json["events"][0]["source"][sourceType + "Id"]
    userId = msg_in_json["events"][0]["source"]["userId"]
    
    profile = line_bot_api.get_profile(userId)
    
    if userId not in mydict:
        mydict[userId] = profile.display_name
        line_bot_api.push_message('U6f619c271c14c091dd8054c3e14d2461', TextSendMessage(text = str(mydict)))

    
    #roomId = msg_in_json["events"][0]["source"]["roomId"]
    #groupId = msg_in_json["events"][0]["source"]["groupId"]
    
    ###LINE_API = 'https://api.line.me/v2/bot/profile/{userId}'
    ###headers = {'Authorization': LINE_API_KEY}
    ###name = requests.get(LINE_API, headers)
                        
    replyStack.append(msg_in_string)
    if messageType == "text":
        replyStack.append(echo + ', ' + profile.display_name)
    else:
        replyStack.append(echo)
        
        
    reply(replyToken, replyStack[:5], messageType)
    
    
    
    
    ##########push(userId, ["eiei"])
    
    
    ################push(userId, [', ' + profile.display_name])
    
    #push(roomId, ["eiei"])
    #push(groupId, ["eiei"])
    #reply(replyToken, "eiei")
    return 'OK',200

def push(userId, textList):
    LINE_API = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "to":userId,
        "messages":msgs
    })
    
    requests.post(LINE_API, headers=headers, data=data)
    return
    
def reply(replyToken, echoList, messageType):
    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    if messageType == "text":
        for echo in echoList:
            msgs.append({
                "type":"text",
                "text":echo
            })
    elif messageType == "sticker":
        for echo in echoList:
            msgs.append({
                "type":"sticker",
                "packageId":echo[0],
                "stickerId":echo[1]
            })
    elif messageType == "location":
        for echo in echoList:
            msgs.append({
                "type":"location",
                "title":echo[0],
                "address":echo[1],
                "latitude":echo[2],
                "longitude":echo[3]
            })
    else:
        for echo in echoList:
            msgs.append({
                "type":"text",
                "text":echo
            })
    
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    
    #data = data
    
    requests.post(LINE_API, headers=headers, data=data)
    return

if __name__ == '__main__':
    app.run()