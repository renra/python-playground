deutsch = {
  10: 'zehn',
  20: 'zwanzig',
  30: 'dreizig'
}

for k, v in deutsch.iteritems():
  print "{0} => {1}".format(k, v)

print deutsch

del deutsch[30]
print deutsch

english = dict([(1, 'one'), (2, 'two'), (3, 'three')])
print english

reverse_english = dict(one=1, two=2)
print reverse_english
