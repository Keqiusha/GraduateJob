# encoding=utf-8

# 导入PcscReader类
from PySmartCard.CpuCard import PcscReader
# 导入time模块
import time


def showLog(data, issend):
    '''打印日志函数'''
    current = time.strftime('%Y_%m_%d %H:%M:%S', time.localtime())
    if issend:  # 发送到卡片的数据
        send = '-->'
    else:  # 卡片返回的数据
        send = '<--'
    print("{} {} {}".format(current, send, data))


def sendApdu(reader, apdu, recv_list, readerType=None):
    '''给卡片发送指令的函数'''
    # 清空
    recv_list[:] = []
    # 去掉多余的空格
    apdu = apdu.replace(' ', '')
    showLog(apdu, True)
    respone = reader.send_apdu(apdu, readerType)
    showLog(respone, False)
    # recv_list第1个元素是返回数据
    recv_list.append(respone[:-4])
    # recv_list第2个元素是sw
    recv_list.append(respone[-4:])


def sendApduCommand(reader, apdu, recv_list, readerType=None):
    '''完整的发送指令函数'''
    sendApdu(reader, apdu, recv_list, readerType)
    # 如果是返回的SW是6CXX或者61XX,重新发指令
    apdu = apdu.replace(' ', '')
    if recv_list[-1][:2] == '61':
        apdu = '00C00000' + recv_list[-1][2:4]
        sendApdu(reader, apdu, recv_list, readerType)
    elif recv_list[-1][:2].upper() == '6C':
        apdu = apdu[:8] + recv_list[-1][2:4]
        sendApdu(reader, apdu, recv_list, readerType)


'''实例化PCSC读卡器'''
pcsc = PcscReader()

'''获取所有的读卡器列表'''
readerName = pcsc.get_pcsc_readerlist()
##print(readerName)#字符串类型的读卡器名称，按;隔开
# 按;切割字符串，得到所有的读卡器名称
print('当前连接的读卡器有：')
readerNameList = readerName.split(';')
for i in range(len(readerNameList) - 1):
    print("{} {} :{}".format('reader', i, readerNameList[i]))

'''连接指定的读卡器'''
print('*' * 40)
# 要连接的读卡器
useReaderName = "SCM Microsystems Inc. SDI010 Contactless Reader 0"
useReaderName = "SCM Microsystems Inc. SDI010 Smart Card Reader 0"

# 得到的是字符串类型的复位信息
ATR = pcsc.connect_device(useReaderName)
if ATR:
    print("ConnectDevice Success...")
    print("ATR: ", ATR)
else:
    print("ConnectDevice Failed!")

'''上电'''
print('*' * 40)
# 通信界面类型： 1-contact reader   2-contactless reader
readerType = 1
if 'Contactless'.lower() in useReaderName.lower():
    readerType = 2
if 0 == pcsc.power_on(readerType):
    print("Device PowerOn Success...")
else:
    print("Device PowerOn Failed!")

'''发送APDU'''
print('*' * 40)
apdu = '00A4 0400 00'
recv_list = []
sendApduCommand(pcsc, apdu, recv_list, readerType)
if recv_list[1] != "9000":
    print("Send Apdu Failed!")

apdu = '0084 0000 08'
recv_list = []
sendApduCommand(pcsc, apdu, recv_list, readerType)
if recv_list[1] != "9000":
    print("Send Apdu Failed!")

'''断开读卡器连接'''
pcsc.disconnect_device()

'''SM4_ECB加密计算'''
print('*' * 40)
encrypt = pcsc.sm4_ecb('0123456789ABCDEFFEDCBA9876543210', '0123456789ABCDEFFEDCBA9876543210', 1)
print(encrypt)
