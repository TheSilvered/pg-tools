import sys; sys.path.insert(0, "..")
from pgt import Stack
import time

s = Stack(1, 2, 3, 4)
print(s, len(s))

for i in s:
    print(i)

print("Stack.push", s.push(2))
print(s, len(s))

print("Stack.pop", s.pop())
print(s, len(s))

print("Stack.peek", s.peek())
print(s, len(s))

print("Stack.is_empty", s.is_empty)

print("Stack.clear", s.clear())
print(s, len(s))

# Enable for checks on memory leaks

# for i in range(1_000_000):
#     s.push(i)
#     print(i)

# time.sleep(10)

# s.clear()
