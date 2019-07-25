my_string = "Ari Bambang Kurniawan"

for character in my_string:
  print(character)

for asdf in my_string:
  print(asdf)

my_list = [1, 2, 5, 3, 9]

for number in my_list:
  print(number)

for number in my_list:
  print(number ** 2)

should_continue = True

while should_continue:
  print("i'm continuing!")

  user_input = input("Should we continue? (y/n)")
  if user_input == "n":
    should_continue = False