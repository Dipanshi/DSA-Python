from queue import PriorityQueue

pq = PriorityQueue()
pq.put((2, "task2"))
pq.put((1, "task1"))
pq.put((3, "task3"))

print(pq.get())  # (1, 'task1')
print(pq.get())  # (2, 'task2')