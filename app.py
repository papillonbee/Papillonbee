from flask import Flask, request, make_response
import json
import requests
import csv
import math
import cmath

response = requests.get('https://gist.githubusercontent.com/papillonbee/227d8a1c26303c815614ade026906b4c/raw/c5b9745ce95d571a40190aa6128ef39973c43dab/rabbit_dictionary.txt')
txt = response.text.replace('\n','|')
txt += '|'
t = ''
Rabbit = []
for i in txt:
    if i == '|':
        Rabbit.append(t)
        t = ''
        continue
    t += i

response = requests.get('https://gist.githubusercontent.com/papillonbee/a18a99a59d9372c9b11e2d1828a26c14/raw/862a3cd0560d94fd1b6e00d6bf5490e96529b3e3/ppllnb.txt')
txt = response.text.replace('\n','|')
txt += '|'
t = ''
ppllnb = []
for i in txt:
    if i == '|':
        ppllnb.append(t)
        t = ''
        continue
    t += i

import numpy, scipy
from gensim import corpora, models, similarities
import pythainlp as tnlp

my_text = [list(filter(lambda a: a != ' ' and a != '  ' and a != '   ', tnlp.word_tokenize(line[:-1].lower()))) for line in Rabbit]
#stoplist = set('i a about an are as at be by com for from how in is it of on or that the this to was what when where who will with the www ไว้ ไม่ ไป ได้ ให้ ใน โดย แห่ง แล้ว และ แรก แบบ แต่ เอง เห็น เลย เริ่ม เรา เมื่อ เพื่อ เพราะ เป็นการ เป็น เปิดเผย เปิด เนื่องจาก เดียวกัน เดียว เช่น เฉพาะ เคย เข้า เขา อีก อาจ อะไร ออก อย่าง อยู่ อยาก หาก หลาย หลังจาก หลัง หรือ หนึ่ง ส่วน ส่ง สุด สําหรับ ว่า วัน ลง ร่วม ราย รับ ระหว่าง รวม ยัง มี มาก มา พร้อม พบ ผ่าน ผล บาง น่า นี้ นํา นั้น นัก นอกจาก ทุก ที่สุด ที่ ทําให้ ทํา ทาง ทั้งนี้ ง ถ้า ถูก ถึง ต้อง ต่างๆ ต่าง ต่อ ตาม ตั้งแต่ ตั้ง ด้าน ด้วย ดัง ซึ่ง ช่วง จึง จาก จัด จะ คือ ความ ครั้ง คง ขึ้น ของ ขอ ขณะ ก่อน ก็ การ กับ กัน กว่า กล่าว'.split())
#my_text = [[word for word in text if word not in stoplist] for text in my_text]
#all_tokens = sum(my_text, [])
#tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
#my_text = [[word for word in text if word not in tokens_once] for text in my_text]

my_dictionary = corpora.Dictionary(my_text)
my_corpus = [my_dictionary.doc2bow(text) for text in my_text]
my_lsi = models.LsiModel(my_corpus, id2word=my_dictionary, num_topics=200)

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
LINE_API_KEY = 'Bearer zbzJP1V5BiTWGBUzUAwSo+139oJZ7LUuHdD2AMP4NMTXl7H37EExGqi6l3ciIs51ESQMGCkmq17KIy/MbSbjhD0abjEAjs4+RlZ3iT7bJlT9qTklgrL5QgXzDn+j5YUj3d6PzMn8ngRHB4ibYf1RpQdB04t89/1O/w1cDnyilFU='

app = Flask(__name__)

line_bot_api = LineBotApi('zbzJP1V5BiTWGBUzUAwSo+139oJZ7LUuHdD2AMP4NMTXl7H37EExGqi6l3ciIs51ESQMGCkmq17KIy/MbSbjhD0abjEAjs4+RlZ3iT7bJlT9qTklgrL5QgXzDn+j5YUj3d6PzMn8ngRHB4ibYf1RpQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c6d40237131458c24f391675e4d8968a')

def calculate_string(s):
    s = s.lower()
    t = ''
    i = 0
    j = 0
    while i < len(s):
        if i + 3 <= len(s) - 1 and s[i] == 'e' and s[i + 1] == 'x' and s[i + 2] == 'p':
            t = t + 'cmath.' + s[i:i+3]
            i = i + 3
        elif i + 3 <= len(s) - 1 and s[i] == 'l' and s[i + 1] == 'o' and s[i + 2] == 'g':
            t = t + 'cmath.' + s[i:i+3]
            i = i + 3
        elif i + 4 <= len(s) - 1 and s[i] == 's' and s[i + 1] == 'i' and s[i + 2] == 'n' and s[i + 3] == 'h':
            t = t + 'cmath.' + s[i:i+4]
            i = i + 4
        elif i + 4 <= len(s) - 1 and s[i] == 'c' and s[i + 1] == 'o' and s[i + 2] == 's' and s[i + 3] == 'h':
            t = t + 'cmath.' + s[i:i+4]
            i = i + 4
        elif i + 4 <= len(s) - 1 and s[i] == 't' and s[i + 1] == 'a' and s[i + 2] == 'n' and s[i + 3] == 'h':
            t = t + 'cmath.' + s[i:i+4]
            i = i + 4
        elif i + 3 <= len(s) - 1 and s[i] == 's' and s[i + 1] == 'i' and s[i + 2] == 'n':
            t = t + 'cmath.' + s[i:i+3]
            i = i + 3
        elif i + 3 <= len(s) - 1 and s[i] == 'c' and s[i + 1] == 'o' and s[i + 2] == 's':
            t = t + 'cmath.' + s[i:i+3]
            i = i + 3
        elif i + 3 <= len(s) - 1 and s[i] == 't' and s[i + 1] == 'a' and s[i + 2] == 'n':
            t = t + 'cmath.' + s[i:i+3]
            i = i + 3
        elif i + 5 <= len(s) - 1 and s[i] == 'a' and s[i + 1] == 's' and s[i + 2] == 'i' and s[i + 3] == 'n' and s[i + 4] == 'h':
            t = t + 'cmath.' + s[i:i+5]
            i = i + 5
        elif i + 5 <= len(s) - 1 and s[i] == 'a' and s[i + 1] == 'c' and s[i + 2] == 'o' and s[i + 3] == 's' and s[i + 4] == 'h':
            t = t + 'cmath.' + s[i:i+5]
            i = i + 5
        elif i + 5 <= len(s) - 1 and s[i] == 'a' and s[i + 1] == 't' and s[i + 2] == 'a' and s[i + 3] == 'n' and s[i + 4] == 'h':
            t = t + 'cmath.' + s[i:i+5]
            i = i + 5
        elif i + 4 <= len(s) - 1 and s[i] == 'a' and s[i + 1] == 's' and s[i + 2] == 'i' and s[i + 3] == 'n':
            t = t + 'cmath.' + s[i:i+4]
            i = i + 4
        elif i + 4 <= len(s) - 1 and s[i] == 'a' and s[i + 1] == 'c' and s[i + 2] == 'o' and s[i + 3] == 's':
            t = t + 'cmath.' + s[i:i+4]
            i = i + 4
        elif i + 4 <= len(s) - 1 and s[i] == 'a' and s[i + 1] == 't' and s[i + 2] == 'a' and s[i + 3] == 'n':
            t = t + 'cmath.' + s[i:i+4]
            i = i + 4
        elif i + 4 <= len(s) - 1 and s[i] == 's' and s[i + 1] == 'q' and s[i + 2] == 'r' and s[i + 3] == 't':
            t = t + 'cmath.' + s[i:i+4]
            i = i + 4
        elif i + 5 <= len(s) - 1 and s[i] == 'g' and s[i + 1] == 'a' and s[i + 2] == 'm' and s[i + 3] == 'm' and s[i + 4] == 'a':
            t = t + 'math.' + s[i:i+5]
            i = i + 5
        elif i + 1 <= len(s) - 1 and s[i] == 'p' and s[i + 1] == 'i':
            t = t + 'cmath.' + s[i:i+2]
            i = i + 2
        elif i <= len(s) - 1 and s[i] == 'x':
            t = t + '^'
            i = i + 1
        elif i <= len(s) - 1 and s[i] == '^':
            t = t + '**'
            i = i + 1
        elif s[i] == 'i':
            t = t + 'j'
            i = i + 1
        elif s[i].isalpha():
            i = i + 1
            j = j + 1
        else:
            t = t + s[i]
            i = i + 1

    try:
        if j > 0:
            raise Exception('UnsupportedCharacter')

        u = eval(t)
        if u.imag == 0:
            print(u.real)
            return u.real
        else:
            print(u)
            return u
    except (SyntaxError, ZeroDivisionError, TypeError, NameError, Exception) as error:
        print(error)
        return None
    
@app.route('/')
def index():
    return 'This is chatbot server.'

@app.route('/bot', methods=['POST'])
def bot():
    #req = request.get_json(silent=True, force=True)
    #res = processRequest(req)
    #res = json.dumps(res, indent=4)
    #r = make_response(res)
    #r.headers['Content-Type'] = 'application/json'
    #return r

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

    sourceType = msg_in_json["events"][0]["source"]["type"]
    Id = msg_in_json["events"][0]["source"][sourceType + "Id"]
    userId = msg_in_json["events"][0]["source"]["userId"]
    
    #replyStack.append(msg_in_string)
    
    if sourceType == "user":
        profile = line_bot_api.get_profile(Id)
    if sourceType == "room":
        profile = line_bot_api.get_room_member_profile(Id, userId)
    if sourceType == "group":
        profile = line_bot_api.get_group_member_profile(Id, userId)
        
    #dic = {}
    #with open('userId.csv', newline = '') as f:
    #    reader = csv.reader(f)
    #    for row in reader:
    #        dic[row[0]] = row[1]
    #if userId not in dic:
    #    with open('userId.csv', 'a' newline = '') as f:
    #        writer = csv.writer(f)
    #        writer.writerow([userId, profile.display_name]
    
    
    
    if messageType == "text":
        x = calculate_string(echo)
        if x is not None:
            echo2 = str(x)
            if x.imag != 0:
                echo2 = echo2.replace('j', 'i')
                echo2 = echo2.replace('(', '')
                echo2 = echo2.replace(')', '')
        else:
            vec_bow = my_dictionary.doc2bow(list(filter(lambda a: a != ' ' and a != '  ' and a != '   ', tnlp.word_tokenize(echo.lower()))))
            vec_lsi = my_lsi[vec_bow]
            my_index = similarities.MatrixSimilarity(my_lsi[my_corpus])
            my_sims = my_index[vec_lsi]
            #echo2 = ppllnb[max(enumerate(my_sims), key=lambda item:item[1])[0]]
            arr = sorted(enumerate(my_sims), key=lambda item: -item[1])[:5]
            echo2 = ppllnb[arr[0][0]]
            top_5_list = ''
            top_5_list += 'Top 5 most similar sentences to \'' + echo + '\':\n'
            for i in range(5):
                top_5_list += str(i+1) + '.) Cosine similarity = ' + str(arr[i][1]) + '\n' + str(Rabbit[arr[i][0]]) + ': ' + str(ppllnb[arr[i][0]])
                if i != 4:
                    top_5_list += '\n'
        line_bot_api.push_message('U6f619c271c14c091dd8054c3e14d2461', TextSendMessage(text = Id + ", " + userId + ", " + profile.display_name + ", " + echo))
        replyStack.append(echo2 + ', ' + profile.display_name)
    else:
        line_bot_api.push_message('U6f619c271c14c091dd8054c3e14d2461', TextSendMessage(text = Id + ", " + userId + ", " + profile.display_name + ", " + str(echo)))
        replyStack.append(echo)
        
        
    if messageType == "text" and echo.lower() == "leave":
        if sourceType == "room":
            line_bot_api.leave_room(Id)
        if sourceType == "group":
            line_bot_api.leave_group(Id)
    else:
        reply(replyToken, replyStack[:5], messageType)
    
    push(Id, [top_5_list])
    #push(Id, [msg_in_string])
    #push(Id, [Rabbit[2079], ppllnb[2079], str(vec_bow)])
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
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0', threaded=True)
