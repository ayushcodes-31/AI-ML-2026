from collections import deque
q=deque()

q.append(10)
q.append(20)

q.popleft()
q.appendleft(30)
print(q)