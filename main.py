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
    list_morceaux = Listbox(bottom_frame, relief='flat', width=80)
    list_morceaux.grid(row=0, rowspan=3, column=1, columnspan=6, padx=60, pady=12)

    morceaux = get_songs("partitions.txt")

    for morceau in morceaux.keys():
        list_morceaux.insert(END, morceau)
    list_morceaux.select_anchor(0)
    list_morceaux.select_set(0)

    btn_lire = Button(bottom_frame, text='Lire un morceau', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                      width=20,
                      command=lambda: play_song("partitions.txt", morceaux[list_morceaux.get(ANCHOR)], 264, 0.125))
    btn_lire.grid(row=0, column=0, sticky=W, pady=10, padx=30)

    btn_composer = Button(bottom_frame, text='Composer', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                          width=20, command=lambda:[compose(main_frame),frame.destroy()])
    btn_composer.grid(row=1, column=0, sticky=W, pady=10, padx=30)

    btn_ajouter = Button(bottom_frame, text='Ajouter un morceau', font=("a_FuturaOrto", 14), bg="#FFB997",
                         relief='flat',
                         width=20, command=lambda:[add_song(main_frame),frame.destroy()])
    btn_ajouter.grid(row=2, column=0, sticky=W, pady=10, padx=30)

    ################ INIT #################

    top_frame.grid(row=0, column=0, sticky=N, pady=80)
    bottom_frame.grid(row=1, column=0, pady=30)

    frame.pack()

def compose(main_frame):
    frame_composer = Frame(main_frame, bg="#5B183C")
    btn_menu= Button(frame_composer, text='Menu', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                          width=20, command=lambda: [main(main_frame), frame_composer.destroy()])
    btn_menu.pack()
    frame_composer.pack()

def add_song(main_frame):
    frame_add_song = Frame(main_frame, bg="#5B183C")
    btn_menu= Button(frame_add_song, text='Menu', font=("a_FuturaOrto", 14), bg="#FFB997", relief='flat',
                          width=20, command=lambda: [main(main_frame), frame_add_song.destroy()])
    btn_menu.pack()
    frame_add_song.pack()

main_frame.pack()
main(main_frame)


fenetre.mainloop()
