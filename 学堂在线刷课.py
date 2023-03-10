import requests
import json
import time

wait = 0.7
d = 2000#视频长度，基本都小于2000s
u = 111111#用户不会变
c = 2563346#每节课会变
skuid = 5740271#每节课会变
classroomid = 12381443 #教室id，每节课会变
cc = '1EBAB282E62D37C29C33DC5901307461'#每节课会变

beforeTheClassroomid = '9nMW3FGBJ3S'#每节课会变
X_CSRFToken = '114514'#用户不会变
cookie = '114514'

vStart = 15717628#第一节课id
vEnd = 15717787#最后一节课id

url = 'https://course.hitsz.edu.cn/video-log/heartbeat/'
headers = {
            'Host': 'course.hitsz.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Content-Type': 'application/json',
            'xtbz': 'cloud',
            'X-CSRFToken': X_CSRFToken,
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://course.hitsz.edu.cn',
            'Connection': 'keep-alive',
            'Content-Length' : '17',
            'Referer': 'https://course.hitsz.edu.cn/pro/lms/',
            'Cookie': cookie,
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
        }
        
for a in range(vEnd - vStart):
    #更新headers
    v = vStart+a
    d = d+1

    headers['Referer'] = 'https://course.hitsz.edu.cn/pro/lms/' + beforeTheClassroomid + '/' + str(classroomid) + '/video/' + str(v)

    #生成发出的json
    dataStr = '{"heart_data":['
    for i in range(int(d/5)):
        dataStr = dataStr + '{"i":5,"et":"heartbeat","p":"web","n":"ali-cdn.xuetangx.com","lob":"cloud4","cp":' + str(i*5) + ',"fp":0,"tp":1,"sp":1,"ts":"' + str(1678360614546 + i*5000) + '","u":' + str(u) + ',"uip":"","c":' + str(c) + ',"v":' + str(v) + ',"skuid":' + str(skuid) + ',"classroomid":"' + str(classroomid) + '","cc":"' + str(cc) + '","d":' + str(d) + ',"pg":"' + str(v) + '_vw2x' + '","sq":' + str(1+i) + ',"t":"video","cards_id":0,"slide":0,"v_url":""},'
    dataStr = dataStr + '{"i":5,"et":"videoend","p":"web","n":"ali-cdn.xuetangx.com","lob":"cloud4","cp":' + str(i*5+5) + ',"fp":0,"tp":1,"sp":1,"ts":"' + str(1678360614546 + i*5000 + 5000) + '","u":' + str(u) + ',"uip":"","c":' + str(c) + ',"v":' + str(v) + ',"skuid":' + str(skuid) + ',"classroomid":"' + str(classroomid) + '","cc":"' + str(cc) + '","d":' + str(d) + ',"pg":"' + str(v) + '_vw2x' + '","sq":' + str(2+i) + ',"t":"video","cards_id":0,"slide":0,"v_url":""}]}'

    #伪装播完时间
    camouflage = '{"heart_data":['
    camouflage = camouflage + '{"i":5,"et":"videoend","p":"web","n":"ali-cdn.xuetangx.com","lob":"cloud4","cp":' + str(100) + ',"fp":0,"tp":1,"sp":1,"ts":"' + str(1678360614546 + i*5000 + 5001) + '","u":' + str(u) + ',"uip":"","c":' + str(c) + ',"v":' + str(v) + ',"skuid":' + str(skuid) + ',"classroomid":"' + str(classroomid) + '","cc":"' + str(cc) + '","d":' + str(d) + ',"pg":"' + str(v) + '_vw2x' + '","sq":' + str(3+i) + ',"t":"video","cards_id":0,"slide":0,"v_url":""}]}'
    
    #转json
    camouflageData = json.loads(camouflage)
    data = json.loads(dataStr)

    #发包
    try:
        ret = requests.post(url = url,headers=headers, json=data)
        print(ret.status_code)
        ret = requests.post(url = url,headers=headers, json=camouflageData)
    except Exception as e:
        print('[Error]: ' + str(e))
    time.sleep(wait)