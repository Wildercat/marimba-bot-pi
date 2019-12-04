import time
import servoActions

def main(song):

    #print(song)

    notes = [servoActions.play0,servoActions.play1,servoActions.play2,servoActions.play3,servoActions.play4]

    for i, beat in enumerate(song):
        #print(i)
        for j, tone in enumerate(beat):
            if tone == 1:
                notes[j]()
        time.sleep(.200)
