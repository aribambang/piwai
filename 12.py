def methodception(another):
  return another()

def add_two_number():
  return 37+77

print(methodception(add_two_number))

print(methodception(lambda: 37+77))

my_list = [2, 10, 19, 97]

def not_two(x):
  return x != 2

print(list(filter(not_two, my_list)))

print([x for x in my_list if x != 2])