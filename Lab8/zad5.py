krawedzie = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'E')]

listaSasiedztwa = {}

for i in krawedzie:
    if i[0] in listaSasiedztwa.keys():
        listaSasiedztwa[i[0]] += "," + i[1]
    else:
        listaSasiedztwa[i[0]] = i[1]

print(listaSasiedztwa)            


