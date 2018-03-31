import pretty_midi


def get_major_scale(note_name):
	note_number = pretty_midi.note_name_to_number(note_name)
	list_note = []
	list_note.append(note_number) 		# I
	list_note.append(note_number + 2) 	# II
	list_note.append(note_number + 4) 	# III
	list_note.append(note_number + 5) 	# IV
	list_note.append(note_number + 7) 	# V
	list_note.append(note_number + 9) 	# VI
	list_note.append(note_number + 11) 	# VII
	return list_note
