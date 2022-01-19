# Author: SMR (AMDG) 01/18/22
def add_last_initial(names,linit):
    x = 0
    for i, v in enumerate(names):
        for ind_2, seat in enumerate(v):
            names[i][ind_2] += " "+ linit[x] + "."
            x += 1
    return names
initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]
rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
rows = add_last_initial(rows, initials)
print(rows)