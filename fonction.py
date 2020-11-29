from time import sleep
import numpy as np
import simpleaudio as sa


def calc_frequency(notes, frequences):
    # TODO
    return


def calc_duration(figures, d0):
    # TODO

    return


def read_line_file(f, num):
    # TODO

    return


def read_sheet():
    # TODO

    return


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
