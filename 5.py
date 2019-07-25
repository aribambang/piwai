known_people = ['Ari', 'Bambang', 'Kurniawan']
person = input('Enter the person you know: ')

if person in known_people:
  print('You know {}!'.format(person))
else:
  print('You dont {}!'.format(person))