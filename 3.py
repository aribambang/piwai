list_variable = ['Ari', 'Bambang', 'Kurniawan']
tuple_variable = ('Ari', 'Bambang', 'Kurniawan') #imutable
set_variable = {'Ari', 'Bambang', 'Kurniawan'} #unique and unordered

print(list_variable)
print(tuple_variable)
print(set_variable)

short_tuple_variable = ("Ari",)
another_short_tuple_variable = "Ari",

print(list_variable[0])
print(tuple_variable[0])
## print(set_variable[0]) # this wont work, cause there is no order. which one is element 0?

list_variable.append('Ganteng')
print(list_variable)

## tuple_variable.append('Ganteng') #this wont work, because a tuple is not a list.
print(tuple_variable)
## tuple_variable[0] = 'can i change this?' #no, u cant

set_variable.add("Ganteng")
print(set_variable)
set_variable.add("Ganteng")
print(set_variable)

##### Set Operations

set_one = {1, 2, 3 ,4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print(set_one.intersection(set_two)) #{1, 3, 5}

print({1, 2}.union({2, 3})) #{1, 2, 3}

print({1, 2, 3, 4}.difference({2,4})) #{1, 3}