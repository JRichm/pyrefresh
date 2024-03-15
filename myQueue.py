# like a stac, the queue is a linear data structure that stores items in a first in first out manner

queue = []

queue.append("a")
queue.append("b")
queue.append("c")
queue.append("d")
print("Initial Queue")
print(queue)

queue.pop(0)
print("POP")
print(queue)

queue.pop(0)
print("POP")
print(queue)

queue.pop(0)
print("POP")
print(queue)

print("Queue after removing elements")
print(queue)