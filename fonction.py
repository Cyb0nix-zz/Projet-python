from time import sleep
import numpy as np
import simpleaudio as sa


def calc_frequencies(notes, f0):
    #Calcul les fréquences des notes donné en fonction de la fréquence du do
    frequency = []
    for note in notes:
        if note == "DO":
            frequency.append(f0)
        elif note == "RE":
            frequency.append(f0 + 33)
        elif note == "MI":
            frequency.append(f0 + 66)
        elif note == "FA":
            frequency.append(f0 + 88)
        elif note == "SOL":
            frequency.append(f0 + 132)
        elif note == "LA":
            frequency.append(f0 + 176)
        elif note == "SI":
            frequency.append(f0 + 231)
        elif note == "Z":
            frequency.append(-1)
        elif note == "":
            frequency.append(frequency[-1])
    return frequency


def calc_duration(figures, d0):
    #Calcule la durée des notes donné en fonction de la durée d'une croche
    durations = []
    for figure in figures:
        if figure == "r":
            durations.append(8 * d0)
        elif figure == "b":
            durations.append(4 * d0)
        elif figure == "n":
            durations.append(2 * d0)
        elif figure == "c":
            durations.append(d0)
        elif figure == "p":
            durations.append((durations[-1]) / 2)

    return durations


def read_line_file(f, num):
    #Lit une ligne spécifique du fichier et la retourne sous forme de chaine de caractère
    file = open(f, "r")
    lignes = file.readlines()

    return lignes[num]


def read_sheet(ligne):
    #Lit une chaine de caractère correspondant a un morceau et la convertie en une liste de durée et une liste de notes qu'elle retopurne
    notes = []
    durations = []

    sheet = ligne.split(" ")

    for note in sheet:
        durations.append(note.rstrip()[-1])
        notes.append(note.rstrip()[:-1])

    return notes, durations

def play_song(f,num,f0,d0):
    #Joue un morceau à partir d'une partition, du numéro du morceau, de la fréquence d'un Do et de la durée d'une croche.

    notes, durations = read_sheet(read_line_file(f,int(num)))
    play_sheet(calc_frequencies(notes, f0), calc_duration(durations, d0))



def play_sheet(frequencies, durations):
    #Joue un morceau à partir d'une liste de frequences et une liste de durée.
    for i in range(len(frequencies)):
        if frequencies[i] == -1:
            sleep(durations[i])
        else:
            sound(frequencies[i], durations[i])

    return


def get_songs(f):
    #Retourne les noms des morceaux contenu dans la partition ainsi que le numéro de leur ligne sous la forme d'un dictionnaire.
    file = open(f, "r", encoding="utf-8")
    lines = file.readlines()
    list_songs = {}
    for line in lines:
        if line[0][0] == "#":
            list_songs[(line.rstrip()[3:])] = (lines.index(line) + 1)

    return list_songs


def sound(freq, duration):
    #Joue un sond en fonction d'une fréquence et de la durée
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
