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
ser.write('AT +CIPGSMLOC=1,1\n;'.encode('UTF-8')) # Command to connect and get the logation function 

