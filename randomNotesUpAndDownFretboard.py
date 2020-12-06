from random import shuffle
from time import sleep
import platform
import sys
import random
from enum import Enum

if platform.system() == "Windows":
    import winsound

metronomeFrequency = 2000  # 2000 Hertz
metronomeDuration = 100  # 100 ms == 0.1 second

bpm = 40
secondsPerBeat = 60 / bpm
reps = 8 # number of times to drill

strings = ["E", "A", "D", "G", "B", "e"]

pattern = Pattern.random
# notes = ["A", "B", "C", "D", "E", "F", "G"] # natural notes
# notes = ["Ab", "Bb", "Db", "Eb", "Gb"] # flats
# notes = ["A#", "C#", "D#", "F#", "G#"] # sharps
notes = ["A", "B", "C", "D", "E", "F", "G", "Ab", "Bb", "Db", "Eb", "Gb", "A#", "C#", "D#", "F#", "G#"]

class Pattern(Enum):

    upDown = "1"
    up = "2"
    down = "3"
    random = "4"

    def getStrings(self):
        if self == Pattern.upDown:
            stringsInReverse = strings[::-1][1:-1]
            return strings + stringsInReverse
        elif self == Pattern.up:
            return strings
        elif self == Pattern.down:
            return strings[::-1]
        elif self == Pattern.random:
            return random.sample(strings, len(strings))

def printStrings(note, currentString):
    for _ in range(6):
        sys.stdout.write("\033[F")

    for string in strings[::-1]:
        if string == currentString:
            if len(note) == 2:
                print(string + "|-" + note + "-|")
            else:
                print(string + "|-" + note + "--|")
        else:
            print(string + "|----|")

# short pause to get read
sleep(2) # seconds

for _ in range(6):
    print()

for _ in range(reps):
    for currentString in pattern.getStrings():
        shuffle(notes)
        printStrings(notes[0], currentString)

        if platform.system() == "Windows":
            sleep(secondsPerBeat - (metronomeDuration / 1000))
            winsound.Beep(metronomeFrequency, metronomeDuration)
        else:
            # I'm guessing the sound caused by printing '\a' is asynchronous? This might screw up the metronome on Mac/Linux 
            sleep(secondsPerBeat)
            print('\a')
            