import time
import checkCurrentSong

try:
    while True:
        checkCurrentSong.main()
        time.sleep(10)

except KeyboardInterrupt:
    print('\n')
