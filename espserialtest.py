import time
import espModule

def handleEspData(data):
    if (data.command == "in"):
        for x in data.data:
            if (len(x) > 6):
                # print(x)
                rfin = {}
                rfin['rfid'] = x.strip()
                rfin['rfidtype'] = '1'
                # sendparam = urlencode(rfin)
                # writegpssql(sendparam)
                espModule.sendCommand('clearin,'+str(x))

    elif (data.command == "out"):
        for x in data.data:
            if (len(x) > 6):
                # print(x)
                rfout = {}
                rfout['rfid'] = x.strip()
                rfout['rfidtype'] = '2'
                # sendparam = urlencode(rfout)
                # writegpssql(sendparam)
                espModule.sendCommand('clearout,'+str(x))

    elif (data.command == "sos"):
        index = 1
        sosState = data.data
        if sosState == "1":
            statusofsos = 1
            espModule.sendCommand('clearsos')

espModule.initialize()
while (True):
    time.sleep(espModule.loopDuration)
    try:
        espModule.sendCommand('isokey')

        espModule.sendCommandWithHandler('in', handleEspData)
        espModule.sendCommandWithHandler('out', handleEspData)
        espModule.sendCommandWithHandler('sos', handleEspData)

        # espModule.sendCommandOnly('clearall')

    except BaseException as e:
        print("***********************************")
        print("...problem... >_" + str(e))
        print("***********************************")
        espModule.closeSerial()
        espModule.initialize()