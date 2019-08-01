import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from email.mime.text import MIMEText      #定义邮件正文
from email.header import Header         #Header()定义邮件标题
from email.mime.multipart import MIMEMultipart
import smtplib
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
    # print(mail_body)
    msg.attach(MIMEText(mail_body, 'html', 'utf-8'))

    '''构造附件'''
    basename = os.path.basename(file_new)
    att = MIMEText(open(file_new, 'rb').read(), 'base64', 'gb2312')
    att['Content-Type'] = 'application/octet-stream'
    att.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', basename))
    msg.attach(att)

    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.exmail.qq.com', '25')
        #'xxx'是邮箱密码，需补充
        smtp.login('liuhl@cloud-young.com', 'xxx')
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
    except:
        print('邮件发送失败！')
    else:
        print('邮件发送成功！')
    finally:
        smtp.quit()


def newReport(testReport):
    '''返回测试报告所在目录下的所有文件列表'''
    lists = os.listdir(testReport)
    '''获得按升序排列后的测试报告列表'''
    lists2 = sorted(lists)
    '''获取最后一个即最新的测试报告地址'''
    file_new = os.path.join(testReport, lists2[-1])
    return file_new


if __name__ == '__main__':

    # 按照一定的格式获取当前的时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")

    # 定义报告存放路径
    test_report = './test_report'
    filename = test_report + '/' + now + 'test_result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title="xxx接口测试报告",
                            description="测试用例执行情况：")

    # 定义测试用例
    test_dir = './test_case'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_t*.py')

    # 运行测试
    runner.run(discover)
    fp.close()
    new_Report = newReport(test_report)
    sendReport(new_Report)