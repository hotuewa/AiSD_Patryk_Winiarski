import numpy as np


#znajdz min i max z macierzy
def znajdz_min_max(macierz):
    x=np.min(macierz)
    y=np.max(macierz)
    print(x)
    print(y)
    min_ind=[]
    max_ind=[]
    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] == x:
                min_ind=[i,j]
            if macierz[i][j] ==y:
                max_ind=[i,j]
    print(macierz[list(max_ind)])



    print(f"Wspolrzedne min: {min_ind} wpolrzedne max: {max_ind}")
    return macierz



macierz = np.array( [
    [5,2,9,8],
    [1,7,3,4],
    [6,0,2,5]
])


print(znajdz_min_max(macierz))


