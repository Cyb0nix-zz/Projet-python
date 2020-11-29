from time import sleep
import numpy as np
import simpleaudio as sa


def calc_frequency(notes):
    frequency = []
    for note in notes:
        if note == "DO":
            frequency.append(264)
        elif note == "RE":
            frequency.append(297)
        elif note == "MI":
            frequency.append(330)
        elif note == "FA":
            frequency.append(352)
        elif note == "SOL":
            frequency.append(396)
        elif note == "LA":
            frequency.append(440)
        elif note == "SI":
            frequency.append(495)
        elif note == "Z":
            frequency.append(-1)
        elif note == "":
            frequency.append(frequency[-1])
    return frequency


def calc_duration(figures, d0):
    durations = []
    for figure in figures:
        if figure == "r":
            durations.append(8*d0)
        elif figure == "b":
            durations.append(4*d0)
        elif figure == "n":
            durations.append(2*d0)
        elif figure == "c":
            durations.append(d0)
        elif figure == "p":
            durations.append((durations[-1])/2)

    return durations


def read_line_file(f, num):
    file = open(f, "r")
    lignes = file.readlines()

    return lignes[num - 1]


def read_sheet(ligne):
    notes_durations = [[], []]

    sheet = ligne.split(" ")

    for note in sheet:
        notes_durations[1].append(note.rstrip()[-1])
        notes_durations[0].append(note.rstrip()[:-1])

    return notes_durations


def play_sheet():
    # TODO

    return


def sound(freq, duration):
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    tone = np.sin(freq * t * 6 * np.pi)
    tone *= 8388607 / np.max(np.abs(tone))
    tone = tone.astype(np.int32)
    i = 0
    byte_array = []
    for b in tone.tobytes():
        if i % 4 != 3:
            byte_array.append(b)
        i += 1
    audio = bytearray(byte_array)
    play_obj = sa.play_buffer(audio, 1, 3, sample_rate)
    play_obj.wait_done()


