import time
# import busio
# import adafruit_pca9685
from adafruit_servokit import ServoKit

# i2c = busio.I2C(board.SCL, board.SDA)
# hat = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(channels=16)

# kit.servo[11].angle = 90
o = 60
c = 80
s = kit.servo[0]

try:
    while True:
        kit.servo[0].angle = o
        time.sleep(.050)
        print(kit.servo[0].angle)
        kit.servo[0].angle = c
        time.sleep(2)
        print(kit.servo[0].angle)
except KeyboardInterrupt:
    kit.servo[0].angle = c
