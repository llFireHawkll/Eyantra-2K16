#! /usr/bin/python
 
# Demo to talk to an XBee ZigBee device
# Per Magnusson, 2015-07-28
  
from xbee import ZigBee
import serial
import serial.tools.list_ports
import time
import sys
 
# Look for COM port that might have an XBee connected
portfound = False
ports = list(serial.tools.list_ports.comports())
print (ports[1][0])
"""
for p in ports:
    # The SparkFun XBee Explorer USB board uses an FTDI chip as USB interface
    if "Silicon Labs" in p[2]:
        print "Found possible XBee on " + p[0]
        if not portfound:
            portfound = True
            portname = p[0]
            print "Using " + p[0] + " as XBee COM port."
        else:
            print "Ignoring this port, using the first one that was found."
"""
if(len(ports)):
    portfound = True
    if portfound:
        ser = serial.Serial(ports[1][0], 9600)
    else:
        sys.exit("No serial port seems to have an XBee connected.")
else:
    portfound = False
 
# Flash the LED attached to DIO1 of the XBee
try:
    xbee = ZigBee(ser)
    print "XBee test"
 
    xbee.at(command='7') # Pin 1 high
    resp = xbee.wait_read_frame()
    print resp
 
    time.sleep(1)
    xbee.at(command='9') # Pin 1 low
    resp = xbee.wait_read_frame()
    print resp
    """
    # Try another AT command
    xbee.at(command='ID')
    resp = xbee.wait_read_frame()
    print resp
    """
    print "Done"
    ser.close()
except:
    print "Error!"
    ser.close()
 
raw_input("Press Enter to continue...")
