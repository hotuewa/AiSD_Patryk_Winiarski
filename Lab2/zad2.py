def znajdz_min_max(macierz):
    min_val = float("+inf")
    max_val = float("-inf")
    min_index = ()
    max_index = ()


    for i in range(len(macierz)):
        for j in range(len(macierz[i])):
            if macierz[i][j] < min_val:
                min_val = macierz[i][j]
                min_index = (i, j)
            if macierz[i][j] > max_val:
                max_val = macierz[i][j]
                max_index = (i, j)

    macierz[min_index[0]][min_index[1]] = "MIN"
    macierz[max_index[0]][max_index[1]] = "MAX"

    for row in macierz:
        print(row)

    return min_val, min_index, max_val, max_index


tablica = [
    [5,2,9,8],
    [1,7,3,4],
    [6,0,2,5]
]

znajdz_min_max(tablica)


