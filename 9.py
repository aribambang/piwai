class Student:
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []

  def average(self):
    return sum(self.marks)/ len(self.marks)
  
  @classmethod
  def go_to_school(cls):
    print("i'm going to school")

  @staticmethod
  def go_to_school1():
    print("i'm going to school")

ari = Student("Ari", "ITB")

ari.marks.append(80)
ari.marks.append(90)
ari.go_to_school()
ari.go_to_school1()

Student.go_to_school1()

# case for example 

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        return cls(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))

store = Store("Amazon")
store.add_item("Keyboard", 160)

Store.franchise(store)
print(Store.store_details(store))
