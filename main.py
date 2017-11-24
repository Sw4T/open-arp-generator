import midi
import random
import constants

# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()
pattern.resolution = 1000

# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)

# Instantiate a MIDI note on event, append it to the track

TICK_IN_SECONDS = 0.0005
NBTICK_FOR_A_SECOND = int(1 / TICK_IN_SECONDS)

# Play a G_3 and a G_2 every second
for i in range(0, 20):

	start_tick = 0
	on = midi.NoteOnEvent(tick=start_tick, velocity=30, pitch=midi.G_3)
	track.append(on)
	on = midi.NoteOnEvent(tick=start_tick, velocity=60, pitch=midi.G_2)
	track.append(on)
	
	# Instantiate a MIDI note off event, append it to the track
	start_tick = NBTICK_FOR_A_SECOND
	off = midi.NoteOffEvent(tick=start_tick, pitch=midi.G_2)
	track.append(off)
	off = midi.NoteOffEvent(tick=start_tick, pitch=midi.G_3)	
	track.append(off)

# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=start_tick + 1)
track.append(eot)
# Print out the pattern
print pattern

# Save the pattern to disk
midi.write_midifile("example.mid", pattern)