import time

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
		timing.main(json.loads(info['data']['song']['data']))
	#else:
		#print('no new song')
try:
    while True:
        checkCurrentSong()
        time.sleep(8)

except KeyboardInterrupt:
    print('\n')
