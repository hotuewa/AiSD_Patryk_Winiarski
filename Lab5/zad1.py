import queue

q = queue.Queue(maxsize=3)

for i in range(3):
    q.put(i + 1)

while not q.empty():
    element = q.get()
    print(element, sep=" ")