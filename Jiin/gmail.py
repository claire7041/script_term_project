# -*- coding: cp949 -*-
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from xml.dom.minidom import getDOMImplementation

#global value
host = "smtp.gmail.com" # Gmail STMP ���� �ּ�.
port = "587"
htmlFileName = "logo.html"
senderAddr = "mjiijm96@naver.com"     # ������ ��� email �ּ�.
recipientAddr = input("���� �̸��� �ּҸ� �Է��ϼ���: ")  # �޴� ��� email �ּ�.
recipientAddr = "hwawon22@naver.com"

msg = MIMEBase("multipart", "alternative")
msg['Subject'] = "���׿��극���� �˻��� ����*^^*"
msg['From'] = senderAddr
msg['To'] = recipientAddr

# MIME ������ �����մϴ�.
name = "Sona"
str1 = "�Ѿ� �ݰ���"
str2 = "^^*"
popo = str1 + "<br>" + str2 + "<br>"
rogod = '0D 0A'
htmlFD = open(htmlFileName, 'w')
htmlFD.write('<html><header></header><body><b>'+name+'</b><br><img src="http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/'+name+'.png"/><p>'+popo+'</p></body></html>')
htmlFD.close()

htmlFD = open(htmlFileName, 'rb')
HtmlPart = MIMEText(htmlFD.read(), 'html', _charset = 'UTF-8')
htmlFD.close()
# ������� mime�� MIMEBase�� ÷�� ��Ų��.
msg.attach(HtmlPart)
# ������ �߼��Ѵ�.
s = mysmtplib.MySMTP(host, port)

s.ehlo()
s.starttls()
s.ehlo()
s.login("kpu12321@gmail.com", "kpu12345")
s.sendmail(senderAddr , [recipientAddr], msg.as_string())
s.close()








































