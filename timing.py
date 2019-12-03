import time
import pygame
import json
import getRequest

def main():
    getRequest.main('https://marimba-bot-259814.appspot.com/api/history/latest')

    f = open('song.json', 'r')
    song = json.loads(f.read())
    f.close

# trellis = range(16)
# song = []
# for thing in trellis:
#     
#     toneList = []
#     notes = range(5)
#     for stuff in notes:
#         toneList.append(0)
#     song.append(toneList)
# 
# song[0][1] = 1
# 
# song[8][4] = 1


    print(song)
    pygame.mixer.init()
    c = pygame.mixer.Sound('tones/c.wav')
    d = pygame.mixer.Sound('tones/d.wav')
    e = pygame.mixer.Sound('tones/e.wav')
    g = pygame.mixer.Sound('tones/g.wav')
    a = pygame.mixer.Sound('tones/a.wav')
    tones = [c,d,e,g,a]
    for i, beat in enumerate(song):
        print(i)
        for j, tone in enumerate(beat):
            if tone == 1:
                tones[j].play()
        time.sleep(.750)