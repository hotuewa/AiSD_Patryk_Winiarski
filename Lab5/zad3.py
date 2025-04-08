def show_queue(x):
    print(x)
def is_empty(x):
    if len(x) > 0:
        return False
    else:
        return True

def enqueue(x):
    pacjent = input("Podaj pacjenta: ")
    q.append(pacjent)

def dequeue(x):
    if not is_empty(x):
        print(x[0])
        x.remove(x[0])
    else:
        print("Kolejka jest pusta")

q = []

print('''\nWybierz dzialanie: 
    1. Zarejestruj pacjenta 
    2. Wywolaj pacjenta do gabinetu 
    3. Pokaz aktualna kolejke 
    4. Zakoncz dzialanie programu''')

while True:
    op = int(input("Co chcesz zrobic? "))
    if op == 1:
        enqueue(q)
    if op == 2:
        dequeue(q)
    if op == 3:
        show_queue(q)
    if op == 4:
        break