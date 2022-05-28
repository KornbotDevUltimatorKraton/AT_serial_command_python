import serial 
ser = serial.Serial("/dev/ttyUSB0")
ser.write('AT +SAPBR = 3,1,"CONTYPE","GPRS"\n;'.encode('UTF-8'))
ser.write('AT +SAPBR = 3,1,"APN","RCMNET"\n;'.encode('UTF-8'))
ser.write('AT +SAPBR = 1,1\n;'.encode('UTF-8'))
ser.write('AT +SAPBR= 1,1\n;'.encode('UTF-8'))
ser.write('AT +SAPBR= 2,1\n;'.encode('UTF-8'))
ser.write('AT +CIPGSMLOC=1,1\n;'.encode('UTF-8'))
ser.write('AT +CIPGSMLOC=1,1\n;'.encode('UTF-8'))
ser.write('AT +CIPGSMLOC=1,1\n;'.encode('UTF-8'))
ser.write('AT +CIPGSMLOC=1,1\n;'.encode('UTF-8'))
ser.write('AT +CIPGSMLOC=1,1\n;'.encode('UTF-8'))
ser.write('AT +CIPGSMLOC=1,1\n;'.encode('UTF-8'))
ser.write('AT +CIPGSMLOC=1,1\n;'.encode('UTF-8'))

if ser.readline().decode('UTF-8').split(" ")[0] == "+CIPGSMLOC:":
              loc = ser.readline().decode('UTF-8').split(" ")[1]
              print("Long,Lat:",loc) # getting the location from the tuple of data 


#Diable sudo usage command 
export DPT_ALLOW_FAKEROOT_OR_SUDO=false
export DPT_CHOWN_FILES=false
export DPT_RESET_SETGID=false
export DPT_SUDO=false
