import smtplib
from email.mime.text import MIMEText
from email.header import Header
def send(msgs,email):
    sender = '1690634654@qq.com'
    receiver = email
    subject = 'python mail'
    smtpsever = 'smtp.qq.com'
    username = '1690634654@qq.com'
    password = 'zetgnxhdeousdegi'
    msg = MIMEText(msgs,'plain','utf-8')
    msg['subject'] = Header(subject,'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.set_debuglevel(1)
    smtp.starttls()
    smtp.login(username,password)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print("succcessed")

