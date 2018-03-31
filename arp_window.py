from Tkinter import *
from arp_properties import *
from arp_maker import *
import constants


class ArpGeneratorWindow(object):

    def __init__(self):
        self.entry_bpm = None
        self.entry_base_note = None
        self.entry_pitch = None

    def generate_arp(self):
        properties = ArpProperties(self.entry_bpm.get(), self.entry_base_note.get(), self.entry_pitch.get())
        arp_maker = ArpMaker(properties)
        random_seq = arp_maker.generate()
        print(properties.__dict__)
        print(random_seq)

    def draw(self):
        main_container_tk = Tk()
        main_container_tk.title("OpenARP Generator v" + constants.VERSION_NUMBER)

        # BPM Layout
        layout_bpm = Frame(main_container_tk, borderwidth=2, relief=GROOVE)
        layout_bpm.pack(padx=8, pady=5)

        label_base_bpm = Label(layout_bpm, text="Beats Per Minute : ")
        label_base_bpm.pack(side=LEFT)
        self.entry_bpm = Entry(layout_bpm, width=5, text="lol")
        self.entry_bpm.pack(side=RIGHT)

        # Base Note Layout
        layout_base_note = Frame(main_container_tk, borderwidth=2, relief=GROOVE)
        layout_base_note.pack(padx=8, pady=5)

        label_base_note = Label(layout_base_note, text="Base note (fundamental) : ")
        label_base_note.pack(side=LEFT)
        self.entry_base_note = Entry(layout_base_note, width=2)
        self.entry_base_note.pack(side=RIGHT)

        # Base Note Pitch Layout
        layout_pitch = Frame(main_container_tk, borderwidth=2, relief=GROOVE)
        layout_pitch.pack(padx=8, pady=5)

        label_pitch = Label(layout_pitch, text="Pitch (1 to 9) : ")
        label_pitch.pack(side=LEFT)
        self.entry_pitch = Entry(layout_pitch, width=2)
        self.entry_pitch.pack(side=RIGHT)

        # Buttons
        quit_button = Button(main_container_tk, text="Quit", command=main_container_tk.quit)
        quit_button.pack(side=BOTTOM)

        generate_button = Button(main_container_tk, text="Generate", command=self.generate_arp)
        generate_button.pack(side=BOTTOM)
        main_container_tk.mainloop()
