#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
# import types
# msg = MIMEText('Hello this is from JYK(by Python)...','plain','utf-8')
msg = MIMEMultipart('alternative')
msg.attach(MIMEText('hello', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))
with open('test.png','rb') as f:
    mime = MIMEBase('image','png',filename='test.png')
    mime.add_header('Content-Disposition','attachment',filename = 'test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
def _format_addr(s):
    name, addr = parseaddr(s)
    # print('\n',name,'\n',addr,'\n')
    return formataddr((Header(name,'utf-8').encode(),addr))
# print(r'check MIMEText\'s type:',type(msg))

# from_addr = input('Plz imput your email address:')
# from_addr_pw = input('Plz input your password:')
# to_addr = input('Tell me who you want this mail to go to:')
# smtp_server = input('Plz tell me your smtp server:')

# from_addr = 'jiangyukuan13@163.com'
# from_addr_pw = 'j1989422dp'
# to_addr = '601688108@qq.com'
# smtp_server = 'smtp.163.com'

from_addr = '601688108@qq.com'
from_addr_pw = 'dzfaqcjrpbkjbfcc'
to_addr = 'jiangyukuan13@163.com'
smtp_server = 'smtp.qq.com'

msg['From'] = _format_addr('This mail is from <%s>' % from_addr)
# msg['To'] = ','.join((_format_addr('Hello <%s>' % to_addr),_format_addr('Hello <Jack@11.com>'),_format_addr('Hello <Mike@22.com>')))
msg['To'] = ','.join((_format_addr('<%s>' % to_addr),_format_addr('<Jack@11.com>'),_format_addr('<Mike@22.com>')))
msg['Subject'] = Header('Say Hi~','utf-8').encode()
 
server = smtplib.SMTP_SSL(smtp_server,'465')
server.set_debuglevel(1)
server.login(from_addr,from_addr_pw)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()