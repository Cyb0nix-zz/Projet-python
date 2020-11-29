from time import sleep
import fonction

sheet = fonction.read_sheet(fonction.read_line_file("partitions.txt",16))

notes = fonction.calc_frequency(sheet[0])
durations = fonction.calc_duration(sheet[1],0.125)

for i in range(len(notes)):
    print(notes[i]," ",durations[i])
    if notes[i] == -1:
        sleep(durations[i])
    else:
        fonction.sound(notes[i], durations[i])


