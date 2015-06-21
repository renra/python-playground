tup1 = (1, 2, 3, 4, 'something')
tup2 = (5, 6, 7)

empty = ()
one_element_tuple = 1,

print tup1, tup2
print tup1[0]

print 1
print one_element_tuple

# Unpacking
x, y, z = tup2

print x
print y
print z

# No no. Tuples are immutable
# tup1[0] = 2
