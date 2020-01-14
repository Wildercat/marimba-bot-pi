import time
import requests
import json
from threading import Thread
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
	playNote(1,50,70)
def play2():
	playNote(2,40,60)
def play3():
	playNote(3,35,55)
def play4():
	playNote(4,35,55)

def timing(song):

    notes = [play0,play1,play2,play3,play4]

    for i, beat in enumerate(song):
        for j, tone in enumerate(beat):
            if tone == 1:
                Thread(target = notes[j]).start()
        time.sleep(.200)

def checkCurrentSong():
	#get latest song
	try:
		r = requests.get('https://marimba-bot-259814.appspot.com/api/history/latest')
	except:
		#print('lost connection')
		return
	info = r.json()
	#open previously played song
	f = open('latest.json', 'r')
	prev = json.loads(f.read())
	f.close()
	#if their IDs don't match, save the new data and play the song
	if info['data']['id'] != prev['data']['id']:
		#print('new song')
		nf = open('latest.json', 'w+')
		nf.write(json.dumps(info))
		nf.close()
		timing(json.loads(info['data']['song']['data']))
	#else:
		#print('no new song')

try: # check the latest song every 8 seconds
    while True:
        checkCurrentSong()
        time.sleep(8)

except KeyboardInterrupt:
    print('\n')
