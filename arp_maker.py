import pretty_midi
import arp_properties
import utils


class ArpMaker:

    def __init__(self, arp_props):
        self.arp_properties = arp_props

    def generate_random_sequence(self):
        pm = pretty_midi.PrettyMIDI(initial_tempo=float(self.arp_properties.bpm))
        note_and_pitch = self.arp_properties.base_note + self.arp_properties.pitch
        list_major_scale = utils.get_major_scale(note_and_pitch)  # TODO Add random computation

        cello_program = pretty_midi.instrument_name_to_program('Cello')
        cello = pretty_midi.Instrument(program=cello_program)
        time_in_seconds = 0

        for note in list_major_scale:
            note = pretty_midi.Note(velocity=100, pitch=note, start=time_in_seconds, end=time_in_seconds + 1)
            cello.notes.append(note)
            time_in_seconds += 1
            print(time_in_seconds)

        pm.instruments.append(cello)
        pm.write('example.mid')
        return list_major_scale



