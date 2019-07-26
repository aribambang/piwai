known_people = ['Ari', 'Bambang', 'Kurniawan']
person = input('Enter the person you know: ')

if person in known_people:
  print('You know {}!'.format(person))
else:
  print('You dont {}!'.format(person))

## for example cases

def who_do_you_know():
  people = input('Enter the names of people you know, separated by commas: ')
  people_list = people.split(',')
  
  people_without_space = []
  for person in people_list:
    people_without_space.append(person.strip())
  
  return people_without_space

def ask_user():
  person = input('Enter a name of someone you know: ')
  if person in who_do_you_know():
    print('You know {}!'.format(person))

ask_user()
