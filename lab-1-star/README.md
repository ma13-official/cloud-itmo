# Лабораторная работа 1 со звездочкой

В рамках выполненгия работы было необходимо попытаться взломать NGINX команды *"жабисты"*

Для попыток взлома были выбраны следующие инструменты:

## 1. Nmap

<details>
    <summary>Попытки взлома</summary>   

    ```bash
    > nmap -p 80,443 first-java.com
    Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-30 15:50 MSK
    Nmap scan report for first-java.com (192.168.0.108)
    Host is up (0.0081s latency).

    PORT    STATE SERVICE
    80/tcp  open  http
    443/tcp open  https

    Nmap done: 1 IP address (1 host up) scanned in 0.08 seconds
    > nmap -sV -p 80,443 first-java.com
    Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-30 15:50 MSK
    Nmap scan report for first-java.com (192.168.0.108)
    Host is up (0.0099s latency).

    PORT    STATE SERVICE  VERSION
    80/tcp  open  http     nginx 1.27.3
    443/tcp open  ssl/http nginx 1.27.3

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 14.54 seconds
    > nmap --script=vuln -p 80,443 first-java.com
    Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-30 15:52 MSK
    Nmap scan report for first-java.com (192.168.0.108)
    Host is up (0.0078s latency).

    PORT    STATE SERVICE
    80/tcp  open  http
    |_clamav-exec: ERROR: Script execution failed (use -d to debug)
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-passwd: ERROR: Script execution failed (use -d to debug)
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    443/tcp open  https
    |_clamav-exec: ERROR: Script execution failed (use -d to debug)
    |_http-csrf: Couldn't find any CSRF vulnerabilities.
    |_http-dombased-xss: Couldn't find any DOM based XSS.
    |_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
    |_sslv2-drown:

    Nmap done: 1 IP address (1 host up) scanned in 112.67 seconds

    > nmap --script ssl-enum-ciphers -p 443 first-java.com
    Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-30 15:56 MSK
    Nmap scan report for first-java.com (192.168.0.108)
    Host is up (0.0082s latency).

    PORT    STATE SERVICE
    443/tcp open  https
    | ssl-enum-ciphers:
    |   TLSv1.2:
    |     ciphers:
    |       TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256 (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA (ecdh_x25519) - A
    |       TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA (ecdh_x25519) - A
    |       TLS_RSA_WITH_AES_256_GCM_SHA384 (rsa 2048) - A
    |       TLS_RSA_WITH_AES_256_CCM_8 (rsa 2048) - A
    |       TLS_RSA_WITH_AES_256_CCM (rsa 2048) - A
    |       TLS_RSA_WITH_ARIA_256_GCM_SHA384 (rsa 2048) - A
    |       TLS_RSA_WITH_AES_128_GCM_SHA256 (rsa 2048) - A
    |       TLS_RSA_WITH_AES_128_CCM_8 (rsa 2048) - A
    |       TLS_RSA_WITH_AES_128_CCM (rsa 2048) - A
    |       TLS_RSA_WITH_ARIA_128_GCM_SHA256 (rsa 2048) - A
    |       TLS_RSA_WITH_AES_256_CBC_SHA256 (rsa 2048) - A
    |       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256 (rsa 2048) - A
    |       TLS_RSA_WITH_AES_128_CBC_SHA256 (rsa 2048) - A
    |       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256 (rsa 2048) - A
    |       TLS_RSA_WITH_AES_256_CBC_SHA (rsa 2048) - A
    |       TLS_RSA_WITH_CAMELLIA_256_CBC_SHA (rsa 2048) - A
    |       TLS_RSA_WITH_AES_128_CBC_SHA (rsa 2048) - A
    |       TLS_RSA_WITH_CAMELLIA_128_CBC_SHA (rsa 2048) - A
    |     compressors:
    |       NULL
    |     cipher preference: server
    |_  least strength: A

    Nmap done: 1 IP address (1 host up) scanned in 2.40 seconds

    > nmap -A -p 80,443 first-java.com
    Starting Nmap 7.80 ( https://nmap.org ) at 2024-11-30 15:56 MSK
    Nmap scan report for first-java.com (192.168.0.108)
    Host is up (0.0091s latency).

    PORT    STATE SERVICE  VERSION
    80/tcp  open  http     nginx 1.27.3
    |_http-server-header: nginx/1.27.3
    |_http-title: Did not follow redirect to https://first-java.com/
    443/tcp open  ssl/http nginx 1.27.3
    |_http-server-header: nginx/1.27.3
    |_http-title: Site doesn't have a title (text/plain;charset=UTF-8).
    | ssl-cert: Subject: commonName=first-app.com/organizationName=Internet Widgits Pty Ltd/stateOrProvinceName=Some-State/countryName=ru
    | Not valid before: 2024-11-29T22:07:21
    |_Not valid after:  2025-11-29T22:07:21
    | tls-alpn:
    |_  http/1.1

    Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
    Nmap done: 1 IP address (1 host up) scanned in 15.24 seconds

    ```
</details>


### 1. **Сканирование открытых портов (порты 80, 443)**:
```bash
nmap -p 80,443 first-java.com
```
- **Прогресс**: Полностью завершен (0.08 секунд).
- **Ошибки**: 0.
- **Результат**: Порты 80 (HTTP) и 443 (HTTPS) открыты на хосте `first-java.com`, что означает, что веб-сервер доступен по этим портам.

### 2. **Определение версии сервисов (Nginx на портах 80 и 443)**:
```bash
nmap -sV -p 80,443 first-java.com
```
- **Прогресс**: Полностью завершен (14.54 секунд).
- **Ошибки**: 0.
- **Результат**: Обнаружен веб-сервер Nginx версии 1.27.3, работающий на портах 80 и 443 (HTTP и HTTPS).

### 3. **Проверка уязвимостей с помощью скриптов Nmap**:
```bash
nmap --script=vuln -p 80,443 first-java.com
```
- **Прогресс**: Полностью завершен (112.67 секунд).
- **Ошибки**: 4 ошибки при запуске скриптов `clamav-exec` и `http-passwd`.
- **Результат**: Нет обнаруженных уязвимостей CSRF, DOM-based XSS или Stored XSS. Однако есть результат по скрипту `sslv2-drown`, который мог бы сигнализировать о наличии слабых алгоритмов в SSL, но это не указано в выводе.

**Что попробовать**:
- Попробовать запустить скрипты с включением режима отладки (`-d`), чтобы понять, почему скрипты не сработали:
  ```bash
  nmap --script=vuln -p 80,443 -d first-java.com
  ```

### 4. **Проверка шифров TLS на порте 443**:
```bash
nmap --script ssl-enum-ciphers -p 443 first-java.com
```
- **Прогресс**: Полностью завершен (2.40 секунд).
- **Ошибки**: 0.
- **Результат**: На порте 443 доступны несколько сильных шифровальных алгоритмов TLS 1.2, включая такие как `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`, `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`, с предпочтением на сервер. Результат показывает, что сервер поддерживает безопасные шифры с хорошим уровнем защиты.

### 5. **Полное сканирование (Service Discovery + OS Detection + Version Detection)**:
```bash
nmap -A -p 80,443 first-java.com
```
- **Прогресс**: Полностью завершен (15.24 секунд).
- **Ошибки**: 0.
- **Результат**: 
  - Обнаружен веб-сервер Nginx версии 1.27.3 на портах 80 и 443.
  - Сертификат для HTTPS выдан для домена `first-app.com` и действителен с 29 ноября 2024 года по 29 ноября 2025 года.
  - Сервер не имеет заданного заголовка для титула страницы на HTTPS, что может свидетельствовать о простоте веб-приложения.

## 2. FFUF

<details>
    <summary>Попытки взлома</summary>   

    ```bash
    > ffuf -u https://first-java.com/FUZZ -w ~/wordlists/common.txt

            /'___\  /'___\           /'___\
        /\ \__/ /\ \__/  __  __  /\ \__/
        \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
            \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
            \ \_\   \ \_\  \ \____/  \ \_\
            \/_/    \/_/   \/___/    \/_/

        v1.1.0
    ________________________________________________

    :: Method           : GET
    :: URL              : https://first-java.com/FUZZ
    :: Wordlist         : FUZZ: /home/ma13/wordlists/common.txt
    :: Follow redirects : false
    :: Calibration      : false
    :: Timeout          : 10
    :: Threads          : 40
    :: Matcher          : Response status: 200,204,301,302,307,401,403
    ________________________________________________

    :: Progress: [4686/4686] :: Job [1/1] :: 669 req/sec :: Duration: [0:00:07] :: Errors: 0 ::
    > ffuf -u https://FUZZ.first-java.com -w ~/wordlists/subdomains.txt -H "Host: FUZZ.first-java.com"

            /'___\  /'___\           /'___\
        /\ \__/ /\ \__/  __  __  /\ \__/
        \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
            \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
            \ \_\   \ \_\  \ \____/  \ \_\
            \/_/    \/_/   \/___/    \/_/

        v1.1.0
    ________________________________________________

    :: Method           : GET
    :: URL              : https://FUZZ.first-java.com
    :: Wordlist         : FUZZ: /home/ma13/wordlists/subdomains.txt
    :: Header           : Host: FUZZ.first-java.com
    :: Follow redirects : false
    :: Calibration      : false
    :: Timeout          : 10
    :: Threads          : 40
    :: Matcher          : Response status: 200,204,301,302,307,401,403
    ________________________________________________

    :: Progress: [1907/1907] :: Job [1/1] :: 18 req/sec :: Duration: [0:01:45] :: Errors: 1907 ::
    > ffuf -u https://first-java.com/index.php\?FUZZ\=value -w ~/wordlists/parameters.txt

            /'___\  /'___\           /'___\
        /\ \__/ /\ \__/  __  __  /\ \__/
        \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
            \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
            \ \_\   \ \_\  \ \____/  \ \_\
            \/_/    \/_/   \/___/    \/_/

        v1.1.0
    ________________________________________________

    :: Method           : GET
    :: URL              : https://first-java.com/index.php?FUZZ=value
    :: Wordlist         : FUZZ: /home/ma13/wordlists/parameters.txt
    :: Follow redirects : false
    :: Calibration      : false
    :: Timeout          : 10
    :: Threads          : 40
    :: Matcher          : Response status: 200,204,301,302,307,401,403
    ________________________________________________

    :: Progress: [2588/2588] :: Job [1/1] :: 287 req/sec :: Duration: [0:00:09] :: Errors: 0 ::

    ```
</details>

### 0. **Подготовка**:
```bash
cd ~
mkdir wordlists
cd wordlists
wget http://ffuf.me/wordlist/common.txt
wget http://ffuf.me/wordlist/parameters.txt
wget http://ffuf.me/wordlist/subdomains.txt
```

- **Результат**: Скачаны необходимые wordlists.

### 1. **Перебор директорий (common.txt)**:
```bash
ffuf -u https://first-java.com/FUZZ -w ~/wordlists/common.txt
```
- **Прогресс**: Полностью завершен (4686 запросов).
- **Ошибки**: 0.
- **Результат**: Нет информации о найденных директориях, так как в выводе отсутствует перечень успешных URL. Это может означать, что все проверенные пути либо возвращали статус 404 (Not Found), либо не подходили под указанные фильтры статуса.

**Что попробовать:**
- Проверить другие wordlists, например, из **SecLists**:
  ```bash
  ffuf -u https://first-java.com/FUZZ -w /path/to/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
  ```
- Расширить список принимаемых статусов с помощью `-mc` (например, включить 404, чтобы видеть все ответы):
  ```bash
  ffuf -u https://first-java.com/FUZZ -w ~/wordlists/common.txt -mc 200,204,301,302,307,401,403,404
  ```

### 2. **Перебор поддоменов (subdomains.txt)**:
```bash
ffuf -u https://FUZZ.first-java.com -w ~/wordlists/subdomains.txt -H "Host: FUZZ.first-java.com"
```
- **Прогресс**: Полностью завершен (1907 запросов).
- **Ошибки**: Все запросы завершились ошибкой, вероятно, **DNS не смог разрешить поддомены** или **сервер возвращает одинаковые ошибки для всех запросов**.

### 3. **Перебор параметров (parameters.txt)**:
```bash
ffuf -u https://first-java.com/index.php?FUZZ=value -w ~/wordlists/parameters.txt
```
- **Прогресс**: Полностью завершен (2588 запросов).
- **Ошибки**: 0.
- **Результат**: Нет вывода о найденных параметрах, это может означать, что ни один из проверенных параметров не дал результата с подходящим HTTP-статусом.

## 3. CURL

<details>
    <summary>Попытки взлома</summary>
    
    ```bash
    > curl -I http://first-java.com/
    HTTP/1.1 301 Moved Permanently
    Server: nginx/1.27.3
    Date: Sat, 30 Nov 2024 13:08:03 GMT
    Content-Type: text/html
    Content-Length: 169
    Connection: keep-alive
    Location: https://first-java.com/

    > curl -I -k https://first-java.com/
    HTTP/1.1 200
    Server: nginx/1.27.3
    Date: Sat, 30 Nov 2024 13:08:45 GMT
    Content-Type: text/plain;charset=UTF-8
    Connection: keep-alive

    > curl -k https://first-java.com/
    Hello World! From first app%
    ```
</details>

### 1. **Проверка редиректа с HTTP на HTTPS**:
```bash
curl -I http://first-java.com/
```
- **Прогресс**: Полностью завершен.
- **Ошибки**: 0.
- **Результат**: Сервер на порту 80 (HTTP) отвечает с кодом состояния 301 (Moved Permanently), что означает, что все запросы на HTTP перенаправляются на HTTPS. Заголовок `Location` указывает на URL `https://first-java.com/`.

### 2. **Проверка заголовков и ответа на HTTPS запрос**:
```bash
curl -I -k https://first-java.com/
```
- **Прогресс**: Полностью завершен.
- **Ошибки**: 0.
- **Результат**: Сервер на порту 443 (HTTPS) отвечает с кодом состояния 200 (OK). Ответ имеет заголовки:
  - **Server**: nginx/1.27.3
  - **Content-Type**: text/plain;charset=UTF-8 (контент типа текстовый, с кодировкой UTF-8)
  - **Connection**: keep-alive (установлено постоянное соединение)
  
  Страница не имеет заголовка `Content-Length`, что может свидетельствовать о динамическом контенте или других особенностях конфигурации сервера. Контент, вероятно, является простым текстом.

## Вывод по результатам выполнения лабораторной работы:

### 1. **Использование Nmap:**
   - Открытые порты 80 (HTTP) и 443 (HTTPS) на сервере `first-java.com` подтвердили наличие веб-сервера Nginx версии 1.27.3.
   - Уязвимости на уровне сервиса не были найдены в ходе сканирования с использованием скриптов Nmap, несмотря на несколько ошибок в скриптах `clamav-exec` и `http-passwd`. Возможное объяснение — это ошибки в их выполнении, которые могут быть устранены с использованием режима отладки (`-d`).
   - Сертификат для HTTPS-соединения действителен с 29 ноября 2024 года по 29 ноября 2025 года и выдан для домена `first-app.com`, что подтверждает наличие SSL-сертификата.
   - Сканирование с использованием скрипта для оценки шифровальных алгоритмов (`ssl-enum-ciphers`) показало, что сервер поддерживает безопасные TLS-шифры (например, `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384` и `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`), что подтверждает высокую безопасность SSL/TLS-конфигурации.

### 2. **Использование FFUF для перебора директорий, поддоменов и параметров:**
   - Попытки перебора директорий с помощью списка `common.txt` не выявили успешных URL, что может указывать на отсутствие общедоступных директорий или на ошибки в настройках фильтрации.
   - Перебор поддоменов с использованием списка `subdomains.txt` не дал результата, что может означать либо блокировку таких запросов, либо отсутствие поддоменов, разрешаемых через DNS.
   - Перебор параметров в URL с помощью списка `parameters.txt` также не привел к обнаружению активных параметров, что может свидетельствовать о безопасности веб-приложения на уровне параметров URL.

### 3. **Использование CURL:**
   - Запрос на порт 80 (HTTP) подтвердил, что сервер перенаправляет все запросы на HTTPS с кодом состояния 301 (Moved Permanently), что является стандартной практикой для улучшения безопасности.
   - HTTPS запрос вернул статус 200 (OK), подтверждая, что сервер доступен по защищенному соединению и содержит простой текстовый контент "Hello World! From first app%".
   - Заголовки ответа подтверждают использование Nginx как веб-сервера, с кодировкой контента UTF-8.
