import pretty_midi


def get_scale(note_name, scale):
	note_number = pretty_midi.note_name_to_number(note_name)
	list_notes = [note_number]
	for mode in scale:
		list_notes.append(note_number + mode)
	print(list_notes)
	return list_notes

