def twice(n):
  return 2*n

def thrice(n):
  3*n    # Oops, forgot return

print(twice(10))
print(thrice(10))

def swap(a, b):
  return b, a     # Look, multiple return

a = 10
b = 20
a, b = swap(a, b)  # Look multiple assignment

print('a is:', a)
print('b is:', b)
