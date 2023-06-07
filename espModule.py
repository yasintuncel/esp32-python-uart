import serial
import time

class SerialParsedData:
  def __init__(self, command, data):
    self.command = command
    self.data = data

port = "COM3"
baudrate = 9600
timeout = 5

loopDuration = 5
commandDuration = 2

global isSerialOpen 
isSerialOpen = False

global globalSerial 

def initialize():
    global globalSerial
    global isSerialOpen
    while (isSerialOpen == False):
        try:
            globalSerial = serial.Serial(port=port, baudrate=baudrate, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False, rtscts=False, dsrdtr=False, timeout=timeout)
            isSerialOpen = True
        except:
            print("***********************************")
            print('Port Acilamadi. Tekrar deniyorum....')
            print("***********************************")
            time.sleep(commandDuration)

def openSerial():
    global globalSerial
    if(globalSerial.is_open == False):
        globalSerial = serial.Serial(port=port, baudrate=baudrate, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, xonxoff=False, rtscts=False, dsrdtr=False, timeout=timeout)

def closeSerial():
    global globalSerial
    global isSerialOpen 
    isSerialOpen = False
    globalSerial.reset_input_buffer()
    globalSerial.reset_output_buffer()
    globalSerial.close()

def parseIncommingData(incommingData):
    strArray = incommingData.replace('\n', '').replace('\r', '').split(",")
    command = strArray[0]
    del strArray[0]
    data = SerialParsedData(command, strArray)
    return data

def sendCommand(command):
    global globalSerial 
    command = command + ","
    print("+ command: " + command + " will send")
    openSerial()
    globalSerial.write(command.encode('utf-8'))
    incommingData = globalSerial.readline()
    print("- DATA: " + str(incommingData).upper())
    print("---------------------------------")
    time.sleep(commandDuration)

def sendCommandWithHandler(command, handler):
    global globalSerial 
    command = command + ","
    print("+ command (Handler): " + command + " will send")
    openSerial()
    globalSerial.write(command.encode('utf-8'))
    incommingData = globalSerial.readline()
    print("- DATA (Handler): " + str(incommingData).upper())
    parsedData = parseIncommingData(incommingData.decode())
    handler(parsedData)
    print("---------------------------------")
    time.sleep(commandDuration)
