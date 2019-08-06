class Student:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks)/len(self.marks)

  @classmethod
  def friend(cls, origin, friend_name, salary):
    return cls(friend_name, origin.school, salary)

class WorkingStudent(Student):
  def __init__(self, name, school, salary):
    super().__init__(name, school)
    self.salary = salary

ari = WorkingStudent("Ari", "ITB", 200.00)
print(ari.salary)

friend = WorkingStudent.friend(ari, "Bambang", 100.00)
print(friend.name)
print(friend.school)
print(friend.salary)