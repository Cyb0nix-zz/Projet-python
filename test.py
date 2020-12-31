import random
sheet = ["MIn", "DOn", "MIn", "DOn", "REc", "MIc", "FAc", "MIn", "REc", "SOLn", "MIn", "DOn", "MIn", "DOn", "MIn",
         "DOn", "REc", "MIc", "FAc", "MIn", "REc", "SOLn", "DOn"]

notes_possible = {}
n_note = 0
for i in range(len(sheet)-1):
    if sheet[i] not in notes_possible:
        notes_possible[sheet[i]] = []
        notes_possible[sheet[i]].append(sheet[i+1])
        n_note += 1
    else:
        if sheet[i+1] not in notes_possible[sheet[i]]:
            notes_possible[sheet[i]].append(sheet[i+1])
print(notes_possible)
keys = []
for key in notes_possible.keys():
    keys.append(key)




premiere_note = random.choice(keys)
print(random.choice(notes_possible[premiere_note]))
print(premiere_note)
