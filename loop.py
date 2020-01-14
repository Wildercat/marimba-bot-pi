import time
import checkCurrentSong

try:
    while True:
        checkCurrentSong.main()
        time.sleep(8)

except KeyboardInterrupt:
    print('\n')
