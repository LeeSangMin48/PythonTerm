# -*- coding: cp949 -*-
#from xmlmovie import *
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer

##global
conn = None
# regKey = '73ee2bc65b*******8b927fc6cd79a97'
regKey = 'daaae38eedaa6adf9766e73211c81cb1'
# 네이버 OpenAPI 접속 정보 information
# server = "openapi.naver.com"
server = "apis.daum.net"
# smtp 정보
host = "smtp.gmail.com"  # Gmail SMTP 서버 주소.
port = "587"


def userURIBuilder(server, **user):
    # str = "http://" + server + "/search" + "?"
    str = "https://" + server + "/contents/movie" + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str


def connectOpenAPIServer():
    global conn, server
    conn = HTTPConnection(server)


def getMovieDataFromTitle(title):
    global server, regKey, conn
    if conn == None:
        connectOpenAPIServer()
    # uri = userURIBuilder(server, key=regKey, query='%20', display="1", start="1", target="book_adv", d_isbn=isbn)
    uri = userURIBuilder(server, apikey=regKey, q=title, output="xml")  # 다음 검색 URL
    conn.request("GET", uri)

    # conn.request("GET", uri)

    req = conn.getresponse()
    print(req.status)
    if int(req.status) == 200:
        print("Movie data downloading complete!")
        return extractMovieData(req.read())
    else:
        print("OpenAPI request has been failed!! please retry")
        return None


def extractMovieData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    print(strXml)
    # Movie 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    print(itemElements)
    for item in itemElements:
        thumbnailElements = item.getiterator("thumbnail")
        titleElements = item.getiterator("title")
        trailerElements = item.getiterator("trailer")
    for thumbnail in thumbnailElements:
        thumbnailContent = thumbnail.find("content")
    for title in titleElements:
        titleContent = title.find("content")
    for trailer in trailerElements:
        trailerlink = trailer.find("link")
    print(title, thumbnailContent, trailerlink)
    if len(title.text) > 0:
        return print({"title": titleContent.text, "thumbnail":thumbnailContent.txt, "trailer":trailerlink.txt})


#def sendMain():
#    global host, port
#    html = ""
#    title = str(input('Title :'))
#    senderAddr = str(input('sender email address :'))
#    recipientAddr = str(input('recipient email address :'))
#    msgtext = str(input('write message :'))
#    passwd = str(input(' input your password of gmail account :'))
#    msgtext = str(input('Do you want to include book data (y/n):'))
#    if msgtext == 'y':
#        keyword = str(input('input keyword to search:'))
#        html = MakeHtmlDoc(SearchMovieTitle(keyword))

#    import mysmtplib
    # MIMEMultipart의 MIME을 생성합니다.
#    from email.mime.multipart import MIMEMultipart
#    from email.mime.text import MIMEText

    # Message container를 생성합니다.
#    msg = MIMEMultipart('alternative')

    # set message
#    msg['Subject'] = title
#    msg['From'] = senderAddr
#    msg['To'] = recipientAddr

#    msgPart = MIMEText(msgtext, 'plain')
#    bookPart = MIMEText(html, 'html', _charset='UTF-8')

    # 메세지에 생성한 MIME 문서를 첨부합니다.
#    msg.attach(msgPart)
#    msg.attach(bookPart)

#    print("connect smtp server ... ")
#    s = mysmtplib.MySMTP(host, port)
    # s.set_debuglevel(1)
#    s.ehlo()
#    s.starttls()
#    s.ehlo()
#    s.login(senderAddr, passwd)  # 로긴을 합니다.
#    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
#    s.close()

    print("Mail sending complete!!!")