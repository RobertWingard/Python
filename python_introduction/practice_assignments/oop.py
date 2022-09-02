#oop
#objects - things, items, they can do things, they have properties / attributes that describe
# emphasizes grouping data and functionality together in entities known as Objects

cat1_data = {
    'name': 'Scar',
    'color': 'dark brown',
    'age': 3,
    'breed': 'lion'
}

cat2_data = {
    'name': 'Garfield',
    'color': 'orange/striped',
    'age': 30,
    'breed': 'lasagna'
}

class Cat():
    all_cats = []
    def __init__(self, cat_data):
        self.name = cat_data['name']
        self.color = cat_data['color']
        self.age = cat_data['age']
        self.breed = cat_data['breed']
        Cat.all_cats.append(self)
    def print_info(self):
        print(f'Name: {self.name} Color: {self.color} Age: {self.age} Breed: {self.breed}')
        return self
    def meow(self):
        print(f'{self.name} lets outs a cry: MEOOOOW')
        return self

cat1 = Cat(cat1_data)
cat2 = Cat(cat2_data)

# print(cat1.name)
# print(cat1.color)

# cat1.print_info().meow()

# print(Cat.all_cats)

for one_cat in Cat.all_cats:
    one_cat.print_info()
