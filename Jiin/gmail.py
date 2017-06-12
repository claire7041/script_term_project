# -*- coding: cp949 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from xml.dom.minidom import getDOMImplementation

#global value
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"
htmlFileName = "logo.html"
senderAddr = "mjiijm96@naver.com"     # 보내는 사람 email 주소.
recipientAddr = input("받을 이메일 주소를 입력하세요: ")  # 받는 사람 email 주소.
recipientAddr = "hwawon22@naver.com"

msg = MIMEBase("multipart", "alternative")
msg['Subject'] = "리그오브레전드 검색한 정보*^^*"
msg['From'] = senderAddr
msg['To'] = recipientAddr

# MIME 문서를 생성합니다.
name = "Sona"
str1 = "뿌액 반가웡"
str2 = "^^*"
popo = str1 + "<br>" + str2 + "<br>"
rogod = '0D 0A'
htmlFD = open(htmlFileName, 'w')
htmlFD.write('<html><header></header><body><b>'+name+'</b><br><img src="http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/'+name+'.png"/><p>'+popo+'</p></body></html>')
htmlFD.close()

htmlFD = open(htmlFileName, 'rb')
HtmlPart = MIMEText(htmlFD.read(), 'html', _charset = 'UTF-8')
htmlFD.close()
# 만들었던 mime을 MIMEBase에 첨부 시킨다.
msg.attach(HtmlPart)
# 메일을 발송한다.
s = mysmtplib.MySMTP(host, port)

s.ehlo()
s.starttls()
s.ehlo()
s.login("kpu12321@gmail.com", "kpu12345")
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()








































