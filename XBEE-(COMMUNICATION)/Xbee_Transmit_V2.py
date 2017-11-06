import serial
"""
PORT = 'COM5'
BAUD_RATE = 9600

UNKNOWN = '\xff\xfe' 
WHERE = '\x00\x13\xA2\x00\x40\xF6\x54\x8B'
dataString='11111222\n'

# Open serial port
ser = serial.Serial(PORT, BAUD_RATE)

zb = ZigBee(ser)

#sends data to xbee address
def sendData(address, datatosend):
    zb.send('tx', dest_addr_long = address, dest_addr = UNKNOWN, data = datatosend)


#test data sending method
while True:
    try:
        sendData(WHERE, dataString)
    except KeyboardInterrupt:
        break


zb.halt()
ser.close()
"""

"""
ser = serial.Serial('COM5', 9600) # open serial port
print(ser.name) # check which port was really used
ser.write('hellosdafasdf') # write a string

ser.close()
"""
"""
with serial.Serial('COM5',9600,timeout=100) as s:
    #s.open()
    #x = s.read() # read one
    s = s.read(10) # read up to ten bytes (timeout)
    line = s.readline()
    print line
"""
"""
from time import sleep
ser = serial.Serial('COM5', timeout=1)
ser.baudrate = 9600

msg = 'ZANE:1:\r'
ser.write(msg)
sleep(0.5)
print ser.readline()
"""
"""
ser = serial.Serial('COM5', 9600, timeout=5)
x = ser.read()          # read one byte
s = ser.read(10)        # read up to ten bytes (timeout)
line = ser.readline()   # read a '\n' terminated line
print line
if line != '\0':
    ser.write('bye')
ser.close()
"""

 
port = "COM5"
baud = 9600
 
ser = serial.Serial(port, baud, timeout=1)
    # open the serial port
if ser.isOpen():
     print(ser.name + ' is open...')
 
while True:
    cmd = raw_input("Enter command or 'exit':")
        # for Python 2
    # cmd = input("Enter command or 'exit':")
        # for Python 3
    if cmd == 'exit':
        ser.close()
        exit()
    else:
        ser.write(cmd.encode('ascii')+'\r')
        out = ser.read(10)
        print('Receiving...'+out)
