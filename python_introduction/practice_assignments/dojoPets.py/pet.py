class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks

    def sleep(self):
        print('increases the pets energy by 25')
    
    def eat(self):
        print('increases the pets energy by 5 & health by 10')

    def play(self):
        print('increases the pets health by 5')

    def noise(self):
        print('roaring sound')

cat = Pet('Bear', 'fat', 'roll')
print(cat)