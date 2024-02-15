from collections import deque

q = deque()
q.append('a')
q.append('b')
# print(q)

q.appendleft('c')
print(q)

print(q.pop())
print(q.popleft())