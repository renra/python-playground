from collections import deque  # More optimal performance than the native list which is slow to pop the first element - has to shift all the others

q = deque(['Something', 'fishy', 'going', 'on'])
q.append('now')
print (q.popleft())
