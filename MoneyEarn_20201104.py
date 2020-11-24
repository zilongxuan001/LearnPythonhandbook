#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
'''
@author: Haffner2010
@contact: myprojtest@example.com
@Software: Pycharm + Python3.6
@OS:Windows 7 64 bit
@Site:https://www.jianshu.com/u/e031670b216b
@file: EmailAutoSend.py
@time: 2018/4/1 20:03
@desc:
'''

#MIME邮件格式分析及信息提取http://www.pythonclub.org/python-files/mime-type
# SMTP模块
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def MySMTP(UserInfo,Message):
    SmtpServer=UserInfo['server']
    user=UserInfo['username']
    port=UserInfo['port']
    Receiver=UserInfo['receiver']
    # print(type(str(Receiver)))
    sender=user # 发件人和登录账户名是同一个地址
    password=UserInfo['password']
    Message['From'] = sender
    Message['To'] = Receiver
    # Message['To'] = ";".join(Receiver)
    # Message['Subject'] = Header(Subject, 'utf-8')
    if port==25:
        smtp=smtplib.SMTP(SmtpServer,port)
    elif(port==465 or port==994):
        smtp = smtplib.SMTP_SSL(SmtpServer, port)  # 使用SSL加密登录，详见http://help.163.com/09/1223/14/5R7P3QI100753VB8.html
    else:
        print('SMTP协议端口号有误，请核对信息！')
    smtp.helo(SmtpServer)
    smtp.ehlo(SmtpServer)
    # smtp.starttls() # 启动安全传输模式
    smtp.login(user, password)
    smtp.sendmail(sender, Receiver, Message.as_string())
    print('Mail sent successfully!')
    smtp.quit()




# 一些基本账户信息的定义
myaccinfo={
    'username':'your_account@example.com', # 登录账户
    'password' : 'Auth Code', # 此为授权码，非登录密码
    'receiver':'your_account@example.com',
    'server' : 'smtp.example.com', # 邮箱服务器地址
    'port':25 # 登录端口号
}




if __name__=="__main__":
    # 邮件信息
    subject = 'subject'
    # 纯文本邮件定义，邮件正文内容
    msg = MIMEText('main body text', 'plain', 'utf-8')
    # 定义发送人，接收人，以及描述信息（主题）
    msg['Subject'] = Header(subject, 'utf-8')
    MySMTP(myaccinfo,msg)