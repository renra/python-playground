ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print ar

# Returns listreverseiterator. Hmmm.
print reversed(ar)
print sorted(ar)

for i, val in enumerate(reversed(ar)):
  print "The value in index {0} is {1}".format(i, val)

for i in ar[:]:
  if i == 8:
    print "Incrementing"
    ar[i] = ar[i] + 1

print ar[1:3]
print ar[:5]
print ar[5:]

print ar[-5]
print ar[-5:-2]

print len(ar)

ar.append(10)
print ar

del ar[9]
print ar

ar[:] = []
print ar

x = [1, 2, 3]
y = ['one', 'two', 'three']

zipped = zip(x, y)
print zipped

for x_val, y_val in zipped:
  print x_val, y_val
