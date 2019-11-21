import time
import pygame

trellis = range(16)
song = []
for thing in trellis:
    
    toneList = []
    notes = range(5)
    for stuff in notes:
        toneList.append(0)
    song.append(toneList)

song[0][1] = 1

song[8][4] = 1
print(song)
pygame.mixer.init()
pygame.mixer.music.load("shorter.wav")
for i, beat in enumerate(song):
    print(i)
    pygame.mixer.music.play()
#     for j, tone in enumerate(beat):
#         if tone == 1:
            
#             print(j)
    time.sleep(.750)