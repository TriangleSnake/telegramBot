try:
    f=open('setting.txt','r',encoding="UTF-8")
    area=f.readline().split('=')[1]
    region=f.readline().split('=')[1]
except:
    print("設定檔有誤")
    exit()


from cgitb import text
import telepot
import sys
import requests
import datetime
import time
import threading
bot=telepot.Bot('---SECRET_TELEBOT_TOKEN---')
starttime = datetime.datetime.now()
print(starttime)
try:
    message="即將發送測試訊息"
    if sys.argv[1]=='test':
        message='即將發送測試訊息'
    else :
        message=region+'地區地震警報:'+sys.argv[1]+'級地震 將於 '+sys.argv[2]+' 秒後抵達'
except:
    pass
area='tn'
ip=requests.get("https://api.ipify.org").text
bot.sendMessage('-592407536',message)
url='---API_URL---?token=ss123'+area+"&ip="+ip
r=requests.get(url)
recieve=r.text

if recieve=='-1':
    print("...訊息已由其他電腦發送...")
    input()
    exit()

recieve=recieve.split(',')
recieve.pop()
for i in recieve:
    print ('發送至:'+str(i))
    try:
        bot.sendMessage(i,message)
        print ('發送成功!')
    except:
        print("發送失敗")
endtime=datetime.datetime.now()
print(endtime)

while 1:
    if int((endtime-starttime).seconds)>=int(sys.argv[2]):
        break
    else :
        time.sleep(int(sys.argv[2])-int((endtime-starttime).seconds))
        break

print('抵達')
for i in range(3):
    bot.sendMessage('-592407536','抵達')
for i in recieve:
    for j in range(3):
        bot.sendMessage(i,'抵達')
url='---API url---'+area
ret=requests.get(url).text
print("伺服器復位訊息:",ret)
url='---API url---'
ret=requests.get(url).text
print("伺服器復位訊息:",ret)
import os
import json
print("等待地震報告中..")
for i in range(480):
    print("\r"+str(480-i)+"秒後取得地震報告",end='')
    time.sleep(1)
url='---API url---'
if requests.get(url).text=='-1':
    print("---地震報告已由其他電腦接手---")
    input()
    exit()

url='https://opendata.cwb.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=---SECRET_API_TOKEN---&format=JSON&areaName=%E8%87%BA%E5%8D%97%E5%B8%82'
r=requests.get(url).text
r=json.loads(r)

print(r)
src=r['records']['earthquake'][0]['reportImageURI']
bot.sendPhoto('-592407536',src)
for i in recieve:
    bot.sendPhoto(i,src)

message='詳細地震報告:\n'+r['records']['earthquake'][0]['web']
bot.sendMessage('-592407536',message)
for i in recieve:
    print ('地震報告發送至:'+str(i))
    bot.sendMessage(i,message)
    print ('發送成功!')
ret=requests.get(url).text
print("伺服器復位訊息:",ret)
print('\n')
os.system('taskkill /f /im chromedriver.exe')
print('--地震預警訊息發送完畢--')
os.system('pause')