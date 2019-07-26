my_set = {1, 3, 5}
my_dict = {'name': 'Ari', 'age': 21, 'grades': [13, 15, 17]}
another_dict = {1: 10, 2: 20, 3: 30}

lottery_player = [{
    'name': 'bambang',
    'numbers': (10, 25, 33, 40)
  },{
    'name': 'bambang',
    'numbers': (10, 25, 33, 40)
  }
]
universities = [
  {
    'name': 'Institut Teknologi Sumatera',
    'location': 'Lampung'
  },
  {
    'name': 'Institut Teknologi Bandung',
    'location': 'Bandung'
  }
]

#sum(lottery_player['numbers'])
#lottery_player['name'] = 'ari'

##

#lottery_player[0].total()
#lottery_player.total()

##

#for example cases

student = { 'name': 'Ari', 'school': 'Computing', 'grades': (66, 77, 88)}

def average_grades(data):
  grades = data['grades']
  return sum(grades)/len(grades)

def average_all_student(student_list):
  total = 0
  count = 0
  for student in student_list:
    total = total + sum(student['grades'])
    count = count + len(student['grades'])
  
  return total/count