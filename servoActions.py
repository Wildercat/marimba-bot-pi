import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

def playNote(srv,open,closed):
	s = kit.servo[srv]
	s.angle = open
	time.sleep(.100)
	s.angle = closed
def play0():
	playNote(0,40,60)
def play1():
	playNote(1,45,65)
def play2():
	playNote(2,40,60)
def play3():
	playNote(3,30,50)
def play4():
	playNote(4,30,50)

#play a scale if ran directly
def main():
	notes = [play0,play1,play2,play3,play4]
	for note in notes:
		note()
		time.sleep(.100)
	time.sleep(.200)
	for rnote in reversed(notes):
		rnote()
		time.sleep(.100)

if __name__ == '__main__':
	main()
