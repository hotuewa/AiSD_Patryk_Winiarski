import queue

q = queue.Queue()
for i in range(3):
    q.put(i + 1)

n = int(input("Podaj ile elementow chcesz zobaczyc: "))
list = []

if q.empty():
    print("Kolejka jest pusta")
else:
    n = min(n, q.qsize())
    for i in range(n):
        list.append(q.get())
    print(list)