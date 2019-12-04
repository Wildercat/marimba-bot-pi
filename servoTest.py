import time
# import busio
# import adafruit_pca9685
from adafruit_servokit import ServoKit

# i2c = busio.I2C(board.SCL, board.SDA)
# hat = adafruit_pca9685.PCA9685(i2c)
kit = ServoKit(channels=16)

# kit.servo[11].angle = 90
o = 50
c = 60
s = kit.servo[1]

try:
    while True:
        s.angle = o
        time.sleep(.100)
        print(s.angle)
        s.angle = c
        time.sleep(2)
        print(s.angle)
except KeyboardInterrupt:
    s.angle = c
