import serial
import sys
import time

print(sys.argv)

device = sys.argv[1]
motor = sys.argv[2]
angle = int(sys.argv[3].rstrip())

print(device)
serialPort = serial.Serial(device)
time.sleep(1)
serialPort.dtr = False
time.sleep(1)
#serialPort.write(bytes([motor]))
print(angle)
if motor is "A":
    print("Motor A")
    print(serialPort.write(b'A'))
elif motor is "B":
    print("Motor B")
    print(serialPort.write(b'B'))
else: print("Motor " + motor + "not found")
print(serialPort.write(bytes([angle])))

serialPort.close()
