##
## Constants for MIDI
##

OCTAVE_MAX_VALUE = 12
OCTAVE_VALUES = range( OCTAVE_MAX_VALUE )

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E','F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
WHITE_KEYS = [0, 2, 4, 5, 7, 9, 11]
BLACK_KEYS = [1, 3, 6, 8, 10]
NOTE_PER_OCTAVE = len(NOTE_NAMES)
NOTE_VALUES = range(OCTAVE_MAX_VALUE * NOTE_PER_OCTAVE)

##
## Application globals
##

VERSION_NUMBER = "0.1"

##
## Scales progression in semi-tones
##

MAJOR_SCALE = [2, 4, 5, 7, 9, 11]
MINOR_SCALE = [2, 3, 5, 7, 8, 10]

