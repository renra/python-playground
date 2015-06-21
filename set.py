unit = set(['John', 'George', 'Paul', 'Frank', 'John'])
print unit

print 'John' in unit
print 'Jack' in unit

ulanbatar_set = set('Ulanbatar')
prague_set = set('Praha')

print ulanbatar_set
print prague_set
print ulanbatar_set - prague_set
print ulanbatar_set | prague_set
print ulanbatar_set & prague_set
print ulanbatar_set ^ prague_set

# Comprehension
upcase_prague_set = {x.upper() for x in prague_set}
print upcase_prague_set
