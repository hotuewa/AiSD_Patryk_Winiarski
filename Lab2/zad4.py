#Napisz funkcję badającą czy dane słowo to palindrom.
from dataclasses import replace


def czy_palindrom(s):
    s=s.replace(" ","").lower()
    if len(s)<=1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return czy_palindrom(s[1:-1])


s=input("Czy podane zdanie to palindrom?")


print(czy_palindrom(s))

