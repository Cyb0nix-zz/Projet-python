# -*- coding: utf-8 -*-
from fonction import *
from tkinter import *

fenetre = Tk()

fenetre.resizable(width=False, height=False)
fenetre.title("Mozarius")
fenetre.geometry("1280x720")
fenetre.iconbitmap("mozarius.ico")
fenetre.config(background="#5B183C")

img_logo = PhotoImage(file="mozarius.png")
main_frame = Frame(fenetre, bg="#5B183C")


def main(main_frame):
    frame = Frame(main_frame, bg="#5B183C")
    top_frame = Frame(frame, bg="#5B183C")
    bottom_frame = Frame(frame, bg="#5B183C")

    ############# top_frame ####################
    image = Canvas(top_frame, width=190, height=190, bg='#5B183C', bd=0, highlightthickness=0)
    image.grid(row=0, column=0, sticky=NE, padx=20)

    logo = image.create_image(0, 0, image=img_logo, anchor=NW)

    title = Label(top_frame, text="Mozarius", font=("a_FuturaOrto", 90), bg='#5B183C', fg='#FFB997')
    title.grid(row=0, column=1, sticky=W, padx=60)

    ############# bottom_frame ###############

    btn_lire = Button(bottom_frame, text='Lire un morceau', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                      width=30,
                      command=lambda: [play(main_frame), frame.destroy()])
    btn_lire.grid(row=0, column=0, sticky=W, pady=10, padx=30)

    btn_composer = Button(bottom_frame, text='Composer', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                          width=30, command=lambda: [compose(main_frame), frame.destroy()])
    btn_composer.grid(row=1, column=0, sticky=W, pady=10, padx=30)

    btn_ajouter = Button(bottom_frame, text='Ajouter un morceau', font=("a_FuturaOrto", 14), bg="#FFB997",
                         relief='flat',
                         width=30, command=lambda: [add_song(main_frame)])
    btn_ajouter.grid(row=2, column=0, sticky=W, pady=10, padx=30)

    ################ INIT #################

    top_frame.grid(row=0, column=0, sticky=N, pady=70)
    bottom_frame.grid(row=1, column=0, pady=30)

    frame.pack()


def play(main_frame):
    frame_play = Frame(main_frame, bg="#5B183C")

    top_frame = Frame(frame_play, bg="#5B183C")
    bottom_frame = Frame(frame_play, bg="#5B183C")

    ############# top_frame ####################
    image = Canvas(top_frame, width=190, height=190, bg='#5B183C', bd=0, highlightthickness=0)
    image.grid(row=0, column=0, sticky=NE, padx=20)

    logo = image.create_image(0, 0, image=img_logo, anchor=NW)

    title = Label(top_frame, text="Mozarius", font=("a_FuturaOrto", 90), bg='#5B183C', fg='#FFB997')
    title.grid(row=0, column=1, sticky=W, padx=60)

    ############# bottom_frame ###############
    list_songs = Listbox(bottom_frame, relief='flat', width=43)
    list_songs.grid(row=0, rowspan=3, column=0)

    songs = get_songs("partitions.txt")
    load_songs(songs,list_songs)

    btn_lire = Button(bottom_frame, text='Lire', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                      width=21,
                      command=lambda: play_song("partitions.txt", songs[list_songs.get(ANCHOR)], 264, 0.125))
    btn_lire.grid(row=4, column=0, sticky=NW, padx=10, pady=10)

    btn_menu = Button(bottom_frame, text='Menu', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                      width=21, command=lambda: [main(main_frame), frame_play.destroy()])
    btn_menu.grid(row=5, column=0, sticky=SW, padx=10)

    image = Canvas(bottom_frame, width=360, height=258, bd=0, highlightthickness=0)
    image.grid(row=0, column=1, sticky=NW, padx=20, rowspan=7)

    ################ INIT #################

    top_frame.grid(row=0, column=0, sticky=N, pady=70)
    bottom_frame.grid(row=1, column=0, pady=20)

    frame_play.pack()


def compose(main_frame):
    frame_composer = Frame(main_frame, bg="#5B183C")

    top_frame = Frame(frame_composer, bg="#5B183C")
    bottom_frame = Frame(frame_composer, bg="#5B183C")

    ############# top_frame ####################
    image = Canvas(top_frame, width=190, height=190, bg='#5B183C', bd=0, highlightthickness=0)
    image.grid(row=0, column=0, sticky=NE, padx=20)

    image.create_image(0, 0, image=img_logo, anchor=NW)

    title = Label(top_frame, text="Mozarius", font=("a_FuturaOrto", 90), bg='#5B183C', fg='#FFB997')
    title.grid(row=0, column=1, sticky=W, padx=60)

    ############# bottom_frame ###############

    list_songs = Listbox(bottom_frame, relief='flat', width=42, height=13, selectmode="multiple")
    list_songs.grid(row=0, rowspan=4, column=1)

    songs = get_songs("partitions.txt")
    load_songs(songs,list_songs)

    btn_inversion = Button(bottom_frame, text='Inversion', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                           width=20,
                           command=lambda: [inversion(songs[list_songs.get(list_songs.curselection()[0])]),load_songs(get_songs("partitions.txt"),list_songs)])
    btn_inversion.grid(row=0, column=0, sticky=W, pady=10, padx=30)

    btn_Markov = Button(bottom_frame, text='Markov', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                        width=20, command=lambda: [markov(get_song_number(list_songs.curselection(),list_songs,songs)),load_songs(get_songs("partitions.txt"),list_songs)])
    btn_Markov.grid(row=1, column=0, sticky=W, pady=10, padx=30)

    btn_Markov2 = Button(bottom_frame, text='Markov 2', font=("a_FuturaOrto", 14), bg="#FFB997",
                         relief='flat',
                         width=20, command=lambda: [markov2(get_song_number(list_songs.curselection(),list_songs,songs)),load_songs(get_songs("partitions.txt"),list_songs)])
    btn_Markov2.grid(row=2, column=0, sticky=W, pady=10, padx=30)

    btn_menu = Button(bottom_frame, text='Menu', font=("a_FuturaOrto", 14), bg="#FFB997",
                      relief='flat',
                      width=20, command=lambda: [main(main_frame), frame_composer.destroy()])
    btn_menu.grid(row=3, column=0, sticky=W, pady=10, padx=30)

    ################ INIT #################

    top_frame.grid(row=0, column=0, sticky=N, pady=70)
    bottom_frame.grid(row=1, column=0, pady=30)
    frame_composer.pack()


main_frame.pack()
main(main_frame)

fenetre.mainloop()
