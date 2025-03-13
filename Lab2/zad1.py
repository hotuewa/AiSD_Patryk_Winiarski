#Znajdz drugą największą wartość z listy

def druga_najwieksza(lista):

    if len(lista)>=2:
        s_list = list(sorted(lista, reverse=True))
        max1 = float("-inf")
        for i in range(len(lista)):
            if s_list[i]==s_list[i+1]:
                s_list[i]=s_list[i+1]

            elif s_list[i]!=s_list[i+1]:
                max1=s_list[i+1]
                return max1
    else:
        return "Lista ma za mało elementów"


print(druga_najwieksza([10,10,10,9]))