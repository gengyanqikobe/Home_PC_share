import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formatdate
import os


#设置登录信息
mail_host = 'smtp.cloud-young.com'
mail_user = 'gengyq@cloud-young.com'
mail_password = 'Gengyanqikobe1'
sender = 'gengyq@cloud-young.com'
receiver = ['gengyanqikobe@163.com']

#设置email信息
#添加一个MINEMutlipart类，处理正文和附件
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver[0]
message['Subject'] = "测试"
message['Date'] = formatdate()

#推荐使用html格式的正文内容，比较灵活，可以附加图片，调整格式
with open("C:\\Users\\hasee\\PycharmProjects\\CloudYoung\\uniteset_lianxi\\_report_html.html",'r') as f:
    content = f.read()
    #content = "lalalallallalalalalalala"

part1 = MIMEText(content,'html','utf-8')

basename = os.path.basename("report.txt")
message.attach(part1)


#



#登录并发送
try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user,mail_password)
    smtpObj.sendmail(sender,receiver,message.as_string())
    print('sucess')
    smtpObj.quit()
except smtplib.SMTPException as e:
    print(e)
