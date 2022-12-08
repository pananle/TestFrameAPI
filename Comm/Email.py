# -*- coding: utf-8 -*-

"""
封装发送邮件的方法
"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(file_path):
    smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
    smtp.login("pan081088@163.com", "CNTCRDZQLNARBFTU")

    smg = MIMEMultipart()
    text_smg = MIMEText("cereshop的接口自动化测试报告", "plain", "utf8")
    smg.attach(text_smg)

    file_msg = MIMEApplication(open(file_path[0], "rb").read())
    file_msg.add_header('content-disposition', 'attachment', filename='接口自动化报告.html')
    smg.attach(file_msg)

    file_msg2 = MIMEText(open(file_path[1], "rb").read(),'base64','utf-8')
    file_msg2.add_header('content-disposition', 'attachment', filename='接口自动化日志.txt')
    smg.attach(file_msg2)

    smg["Subject"] = "接口自动化测试"
    smg["From"] = "pan081088@163.com"
    smg["To"] = "pan081888@163.com"
    smtp.send_message(smg, from_addr="pan081088@163.com", to_addrs="pan081888@163.com")

