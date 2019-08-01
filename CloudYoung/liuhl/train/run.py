# -*- coding: utf-8 -*-
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText      #定义邮件正文
from email.header import Header         #Header()定义邮件标题
from email.mime.multipart import MIMEMultipart

import smtplib
import unittest
import time
import os


def sendReport(file_new):

    '''构造邮件'''
    msg = MIMEMultipart()
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = 'liuhl@cloud-young.com'
    msg['To'] = 'liuhl@cloud-young.com'

    '''构造邮件正文'''
    with open(file_new, 'rt') as f:
        mail_body = f.read()
        f.close()
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))

    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com', '25')
    # 'xxx'是邮箱密码，需补充
    smtp.login('liuhl@cloud-young.com', 'xxx')
    smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp.quit()

if __name__=='__main__':
    test_dir = '/Users/yrzty/PycharmProjects/train/testcases'
    test_report = '/Users/yrzty/PycharmProjects/train/reports'

    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_t*.py')

    now = time.strftime('%Y%m%d %H%M%S')

    filename = test_report + '/' + now + 'result.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()
    sendReport(filename)







    '''延展问题
    1.如何在邮件中添加附件
    2.存在多个报告时怎么获取最新的报告
    3.存在多个测试文件时怎么运行
    '''