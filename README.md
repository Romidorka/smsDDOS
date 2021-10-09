# smsDDOS

smsDDOS - это программа для SMS спамминга.

## Установка

Для Termux:

```bash
pkg install python3 tor git
pip3 install -r requirements.txt
cd ~
git clone https://github.com/Romidorka/smsDDOS
```

## Настройка Tor

**Если вам не нужен Tor, можете пропустить этот пункт**

Для Termux:

```bash
cd ~/../usr/etc/tor/
cp torrc torrc.backup
tor --hash--password password
```
Вам выведется хеш пароля, его необходимо скопировать.
```bash
nano torrc
```

Находим строчку где написанно:
```#HashedControlPassword```, стираем знак решотки (#) и то, что написано после
```HashedControlPassword```.

Вставляем ранее скопированный хеш пароля.
Чтобы сохранить, нажимаем Ctrl + O, потом Enter.

Выходим - Ctrl + X

## Запуск

Для Termux:

### Запускаем Tor

**Если вам не нужен Tor, можете пропустить этот подпункт.**

Если вы хотите использовать Tor, то его надо запустить.
Создаём новую сессию (свайп в право, кнопка NEW SESSION), пишем:

```bash
tor
```

Далее переключаемся на первую сессию и запускаем smsDDOS.

### Запускаем smsDDOS

```bash
cd ~/smsDDOS
python3 main.py
```
