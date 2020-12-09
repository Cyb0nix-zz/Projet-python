from time import sleep
import fonction

notes,durations = fonction.read_sheet(fonction.read_line_file("partitions.txt",14))

fonction.play_sheet(fonction.calc_frequency(notes,264),fonction.calc_duration(durations,0.125))


