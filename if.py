num = int(raw_input('Gimme a number: '))

if(num > 0 and num < 10):
  print('Hmm, a very small number indeed')
elif(num < 0):
  print('That is a negative number')
else:
  print('This number is greater than 10. Cooool!')
