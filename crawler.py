import socket, time, re

def connect_to_server(ip, port, retry = 10):
    s = socket.socket()
    try:
        s.connect((ip, port))
    except Exception as e:
        print(e)
        if retry > 0:
            time.sleep(1)
            retry -=1
            connect_to_server(ip, port, retry)
        
    return s

def get_source(s, ip, page):
    CRLF = '\r\n'
    get = 'GET /' + page + ' HTTP/1.1' + CRLF
    get+= 'Host: '
    get += ip
    get += CRLF
    get += CRLF
    #print(get)
    s.send(get.encode('utf-8'))
    response = s.recv(10000000).decode('latin-1')
    #print(response)
    return response

def get_all_links(response):
    list_link = []
    beg = 0
    href = 'href="'
    while True:
        beg_str = response.find(href, beg)
        if(beg_str == -1):
            return list_link
        end_str = response.find('"', beg_str + 6)
        link = response[beg_str + 6:end_str]
        if link not in list_link:
            list_link.append(link)
        beg = end_str + 1

ip = 'www.crawler-test.com'
port = 80
page = '/'
list_link = []
list_link2 = []
cnt = 0
s = connect_to_server(ip, port)
print(s)
response = get_source(s, ip, page)
print(get_all_links(response))
list_link = get_all_links(response)
for link in list_link:
    print(link)
    page2 = page + link
    response = get_source(s, ip, page2)
    if response.find('200 OK', 0):
        list_link2 = get_all_links(response)
        for link in list_link2:
            print(link)
            response = get_source(s, ip, page2)
            if(get_source):
                cnt+=1
            if cnt >=50:
                break
print(len(list_link))
            



