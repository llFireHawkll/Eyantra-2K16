#!/usr/bin/python
import serial

#router port
PORT = 'COM5'
BAUD_RATE = 9600
ser = serial.Serial(PORT, BAUD_RATE)

#myaddress - its the router
ack='0013A20040F6549D'

while True:
    incoming = ser.readline().strip()
    if incoming != '0013A20040F6549D':
        print '%s' % incoming
        ser.write('%s' % ack)

ser.close()
