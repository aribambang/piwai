def print_method(my_parameter):
  print(my_parameter)

def multiplication_method(args1, args2):
  return args1*args2

result = multiplication_method(5, 3)
print(result)

print_method(multiplication_method(5,3))