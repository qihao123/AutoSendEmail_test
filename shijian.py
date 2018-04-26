from youjian import send
import time
t = False
def times():
    a = time.strftime("%H%M",time.localtime())
    return a
def sendmsg(times1,msg):
    a = times()
    a = str(a)
    if a == str(times1):
        email = '1047355811@qq.com'
        msgs = msg
        send(msgs,email)
        time.sleep(60)
        sendmsg(times1,msg)
    else:

        time.sleep(30)
        sendmsg(times1,msg)
msg = 'abcdefghijklmn'
times1 = 2359
sendmsg(times1,msg)