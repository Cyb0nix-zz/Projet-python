from time import sleep
import fonction

sheet = fonction.read_sheet(fonction.read_line_file("partitions.txt",14))

notes = fonction.calc_frequency(sheet[0])
durations = fonction.calc_duration(sheet[1],0.125)

fonction.play_sheet(notes,durations)


