import pretty_midi
import arp_properties
import scales
import matrix
from sequence_generator import *


class ArpMaker(object):

    def __init__(self, arp_props):
        self.arp_properties = arp_props

    def generate(self):
        pm = pretty_midi.PrettyMIDI(initial_tempo=float(self.arp_properties.bpm))
        note_and_pitch = self.arp_properties.base_note + self.arp_properties.pitch
        list_major_scale = scales.get_major_scale(note_and_pitch)
        midi_sequence = self.get_random_midi_sequence(16, list_major_scale)
        print("Generated MIDI sequence : " + ''.join(str(midi_sequence)))

        cello_program = pretty_midi.instrument_name_to_program('Cello')
        cello = pretty_midi.Instrument(program=cello_program)
        time_in_seconds = 0

        for note in midi_sequence:
            note = pretty_midi.Note(velocity=100, pitch=note, start=time_in_seconds, end=time_in_seconds + 1)  # TODO True bpm
            cello.notes.append(note)
            time_in_seconds += 1

        pm.instruments.append(cello)
        pm.write('example.mid')
        return list_major_scale

    def get_random_midi_sequence(self, nb_sequence, list_scale):
        midi_sequence = []
        random_matrix = matrix_random_walk(matrix.ALPHA_ONE_7_7, nb_sequence, 0, 0)
        print("Random path matrix : " + ''.join(str(random_matrix)))
        print("MIDI major scale of " + (self.arp_properties.base_note + self.arp_properties.pitch) + " : " + ''.join(str(list_scale)))
        for i in range(nb_sequence + 1):
            midi_sequence.append(list_scale[random_matrix[i] - 1])

        return midi_sequence
