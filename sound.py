import winsound
import time

LOWC, D, E, F, G, A, B, HIGHC = 262, 294, 330, 349, 392, 440, 494, 523 # Hz
DURATION = 500 # milliseconds
PAUSE = 0.1 # seconds

solfege = [LOWC, D, E, F, G, A, B, HIGHC]

for note in solfege:
    winsound.Beep(note, DURATION)
    time.sleep(PAUSE)