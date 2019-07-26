lottery_player_dict = {
  'name': 'Ari',
  'numbers': (1, 23, 4, 52)
}

class LotteryPlayer:
  def __init__(self, name):
    self.name = name
    self.numbers = (1, 23, 4, 52)

  def total(self):
    return sum(self.numbers)

player_one = LotteryPlayer('Ari')
player_one.numbers = (1, 2, 3, 6, 7 ,8)
player_two = LotteryPlayer('Bambang')

print(player_one == player_two)

## for example cases

# cases 1 (Student)
class Student:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks)/len(self.marks)

ari = Student('Ari', 'ITERA')
ari.marks.append(70)
ari.marks.append(80)
print(ari.average())

# cases 2 (Store)
class Store:
  def __init__(self, name):
    self.name = name
    self.items = []

  def add_item(self, name, price):
    item = {'name': name, 'price': price}
    self.items.append(item)

  def stock_price(self):
    return sum(item['price'] for item in self.items)