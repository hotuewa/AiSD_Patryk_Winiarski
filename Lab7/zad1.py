def wyszukiwanieLiniowe(lista, poszukiwanaLiczba):

    if len(lista) <= 0:
        return -1
    else:
        wynik = []
        for i in range(len(lista)):
            if lista[i] == poszukiwanaLiczba:
                wynik.append(i)
        return wynik[0]        
    
    
       



print(wyszukiwanieLiniowe([],6))



