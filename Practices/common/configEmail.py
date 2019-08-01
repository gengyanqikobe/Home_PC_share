import os
import Practices.readConfig as readConfig
from datetime import datetime
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import zipfile
import glob
localReadConfig = readConfig.ReadConfig()

class Email:
    def __init__(self):

        global host,port,user,password,sender,subject,content,testuser,title
        host = localReadConfig.get_email('mail_host')
        port = localReadConfig.get_email('mail_port')
        user = localReadConfig.get_email('mail_user')
        password = localReadConfig.get_email('mail_password')
        sender = localReadConfig.get_email('sender')
        content = localReadConfig.get_email('content')
        title = localReadConfig.get_email('title')
        self.value = localReadConfig.get_email('receiver')
        self.receiver = []
        #获得receiver列表
        for rece in self.value.split('/'):
            self.receiver.append(rece)
        date = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        self.subject =title +' ' + date
        self.msg = MIMEMultipart('mixed')

    def config_header(self):
        self.msg['subject'] = self.subject
        self.msg['from'] = sender
        self.msg['to'] = ';'.join(self.receiver)

    def config_content(self):
        content_plain = MIMEText(content,'plain','utf-8')
        self.msg.attach(content_plain)

    def send_email(self):
        self.config_header()
        self.config_content()
        try:
            smtp = smtplib.SMTP()
            smtp.connect(host)
            smtp.login(user,password)
            smtp.sendmail(sender,self.receiver,self.msg.as_string())
            smtp.quit()
            print('报告已经发送')
        except Exception as f:
            print(f)


class MyEmail:
    email = None
    mutex = threading.Lock()

    def __init__(self):
        pass
    @staticmethod
    def get_email():
        if MyEmail.email is None:
            MyEmail.mutex.acquire()
            MyEmail.email = Email()
            MyEmail.mutex.release()
        return MyEmail.email

if __name__ == '__main__':
    email = MyEmail.get_email()
