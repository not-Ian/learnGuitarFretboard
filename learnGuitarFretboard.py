from random import shuffle
from time import sleep
import platform

if platform.system() == "Windows":
    import winsound

metronomeFrequency = 2000  # 2000 Hertz
metronomeDuration = 100  # 100 ms == 0.1 second

beatsPerNote = 11 # 6 if you only go up the strings once, 11 if you go up then down, etc
bpm = 80
secondsPerBeat = 60 / bpm

notes = ["A", "B", "C", "D", "E", "F", "G", "Ab", "Bb", "Db", "Eb", "Gb", "A#", "C#", "D#", "F#", "G#"]
shuffle(notes)

# short pause to get ready
sleep(2) # seconds

for note in notes:
    print(note)

    # short pause to see what note is next
    sleep(1.5) # seconds

    for _ in range(beatsPerNote):
        if platform.system() == "Windows":
            winsound.Beep(metronomeFrequency, metronomeDuration)
            sleep(secondsPerBeat - (metronomeDuration / 1000))
        else:
            # I'm guessing the sound caused by printing '\a' is asynchronous? Might screw up the metronome on Mac/Linux 
            print('\a')
            sleep(secondsPerBeat)