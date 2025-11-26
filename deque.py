from collections import deque as dq

a = dq([1, 2, 3, 4, 5])
print(type(a))
a.append(int(input("Число --> ")))
b = a.popleft()
print(a, b)
c = dq([])
for i in a:
   i += 100
   c.appendleft(i)
print(c)