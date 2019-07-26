my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)]
multiply_list = [x * 3 for x in range(5)]

print(an_equal_list)
print(multiply_list)
print([n for n in range(10) if n % 2 == 0])

people_you_know = ["Ari", "bambang", "KURNIAWAN"]
normalised_people = [person.strip().lower() for person in people_you_know]
print(normalised_people)

## for example cases

def who_do_you_know():
  people = input('Enter the names of people you know, separated by commas: ')
  people_list = people.split(',')
  
  people_without_space = [person.strip() for person in people_list]
  
  return people_without_space

def ask_user():
  person = input('Enter a name of someone you know: ')
  if person in who_do_you_know():
    print('You know {}!'.format(person))

ask_user()