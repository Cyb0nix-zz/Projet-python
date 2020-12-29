# -*- coding: utf-8 -*-
from time import sleep
import numpy as np
import random
import simpleaudio as sa
from tkinter import filedialog
from tkinter import *
import random

def calc_frequencies(notes, f0):
    # Calcul les fréquences des notes donné en fonction de la fréquence du do
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
    # Calcule la durée des notes donné en fonction de la durée d'une croche
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
    # Lit une ligne spécifique du fichier et la retourne sous forme de chaine de caractère
    file = open(f, "r")
    lines = file.readlines()

    return lines[num]


def read_sheet(line):

    # Lit une chaine de caractère correspondant a un morceau et la convertie en une liste de durée et une liste de
    # notes qu'elle retourne

    notes = []
    durations = []

    sheet = line.split(" ")



    for note in sheet:
        durations.append(note.rstrip()[-1])
        notes.append(note.rstrip()[:-1])

    return notes, durations


def play_song(f, num, f0, d0):
    # Joue un morceau à partir d'une partition, du numéro du morceau, de la fréquence d'un Do et de la durée d'une
    # croche.

    notes, durations = read_sheet(read_line_file(f, num))
    play_sheet(calc_frequencies(notes, f0), calc_duration(durations, d0))


def play_sheet(frequencies, durations):
    # Joue un morceau à partir d'une liste de frequences et une liste de durée.
    for i in range(len(frequencies)):
        if frequencies[i] == -1:
            sleep(durations[i])
        else:
            sound(frequencies[i], durations[i])

    return


def get_songs(f):
    # Retourne les noms des morceaux contenu dans la partition ainsi que le numéro de leur ligne sous la forme d'un
    # dictionnaire.
    file = open(f, "r", encoding="utf-8")
    lines = file.readlines()
    songs = {}
    for line in lines:
        if line[0][0] == "#":
            songs[(line.rstrip()[1:])] = (lines.index(line) + 1)

    return songs


def load_songs(songs,list_songs):

    list_songs.delete(0,500)
    for song in songs.keys():
        list_songs.insert(END, song)
    list_songs.select_anchor(0)
    list_songs.select_set(0)

def get_song_number(list_select,list_songs,songs):
    songs_numbers = []
    for nbr in list_select:
        songs_numbers.append(songs[list_songs.get(nbr)])

    return songs_numbers


def inversion(line):
    print(line)
    sheet = read_line_file("partitions.txt", line).rstrip().split(" ")
    name = "#" + str(len(get_songs("partitions.txt")) + 1) + " Inversion " + (
        read_line_file("partitions.txt", line - 1).rstrip()[3:]) + "\n"

    sheet2 = sheet.copy()
    for i in range(len(sheet)):
        sheet2[(len(sheet) - 1) - i] = sheet[i]

    file_2 = open("partitions.txt", "a", encoding="utf-8")
    file_2.write(name)
    file_2.write(" ".join(sheet2) + "\n")


def markov(list_of_songs):
    songs = ""
    new_song = []
    keys = []
    notes_possible = {}

    name = "#" + str(len(get_songs("partitions.txt")) + 1) + " Markov"

    for element in list_of_songs:
        songs = read_line_file("partitions.txt", element).rstrip() + " " + songs
        name = name + " | " + (read_line_file("partitions.txt", element-1).rstrip()[3:])

    sheet = songs.strip().split(" ")

    for i in range(len(sheet) - 1):
        if sheet[i] not in notes_possible:
            notes_possible[sheet[i]] = []
            if sheet[i + 1] != sheet[-1]:
                notes_possible[sheet[i]].append(sheet[i + 1])
        else:
            if sheet[i + 1] not in notes_possible[sheet[i]]:
                if sheet[i + 1] != sheet[-1]:
                    notes_possible[sheet[i]].append(sheet[i + 1])

    for key in notes_possible.keys():
        keys.append(key)

    new_song.append(random.choice(keys))

    for i in range(len(sheet) - 1):
        new_song.append(random.choice(notes_possible[new_song[-1]]))

    file_2 = open("partitions.txt", "a", encoding="utf-8")
    file_2.write(name + "\n")
    file_2.write(" ".join(new_song) + "\n")


def markov2(list_of_songs):
    songs = ""
    new_song = []
    max = 0
    val = ""
    notes_possible = {}
    occurences = {}

    name = "#" + str(len(get_songs("partitions.txt")) + 1) + " Markov 2"

    for song in list_of_songs:
        songs = read_line_file("partitions.txt", song).rstrip() + " " + songs
        name = name + " | " + (read_line_file("partitions.txt", song-1).rstrip()[3:])

    sheet = songs.strip().split(" ")

    for i in range(len(sheet) - 1):
        if sheet[i] not in notes_possible:
            notes_possible[sheet[i]] = []
            if sheet[i + 1] != sheet[-1]:
                notes_possible[sheet[i]].append(sheet[i + 1])
            occurences[sheet[i]] = 1
        else:
            if sheet[i + 1] != sheet[-1]:
                notes_possible[sheet[i]].append(sheet[i + 1])
            occurences[sheet[i]] += 1

    for element in occurences.keys():
        if occurences[element] > max:
            val = element

    new_song.append(val)

    for i in range(len(sheet) - 1):
        new_song.append(random.choice(notes_possible[new_song[-1]]))

    file_2 = open("partitions.txt", "a", encoding="utf-8")
    file_2.write(name + "\n")
    file_2.write(" ".join(new_song) + "\n")


def sound(freq, duration):
    # Joue un son en fonction d'une fréquence et de la durée
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



def add_song(fenetre):
    fenetre.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(("texte files", "*.txt"), ("all files", "*.*")))

    file_1 = open(fenetre.filename, "r", encoding="utf-8")
    file_2 = open("partitions.txt", "a", encoding="utf-8")

    lines_1 = file_1.readlines()
    for line in lines_1:
        file_2.write(line)

