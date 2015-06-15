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

# I can do better, of course
a, b = b, a

print('Now a is:', a)
print('Now b is:', b)

#Here is the devil - an array is a referenced object which means
#  it will be defaulted only once
def append(element, list = []):
  list.append(element)
  return list

def fixed_append(element, list = None):
  if list is None:
    list = []

  list.append(element)
  return list

ar = [1, 2, 3]
print append(4, ar)

print append(1)
print append(1) #returns [1, 1] because 1 has been added to the default list already

print fixed_append(1)
print fixed_append(1) #returns [1] because the default empty array is created at every call

def print_one_two_and_three(language_name, one, two, three = 'three'):
  print 'In the ' + language_name + ' language one is ' + one + ', two is ' + two + ' and three is ' + three

print_one_two_and_three('English', 'one', 'two')
print_one_two_and_three('German', 'einz', 'zwei', 'drei')

#Look, I can be specific
print_one_two_and_three(language_name='Dutch', one='een', two='twei', three='drie')

def print_splat(*array):
  for element in array:
    print element

print_splat('Mary', 'had', 'a', 'little', 'lamb')
print_splat(['Mary', 'had', 'a', 'little', 'lamb'])

def print_dict(language_name, **dict):
  for key in dict.keys():
    print 'In the ' + language_name + ' language ' + key + ' is ' + dict[key]

print_dict('Deutsch', buy='kaufen', speak='sprechen')

#Lambdas
operation = lambda x, y: x + y
print operation(10, 1)
