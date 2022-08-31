from character import Character

class Pokemon(Character):
    def __init__(self, type, hp):
        super().__init__()
        self.type = type
        self.health = hp
        self.strength = 5

    def level_up(self):
        self.level +=1
        self.strength += 1
        self.defense += 1
    
    def print_info(self):
        super().print_info()
        print(self.type)



bulbasaur = Pokemon('grass', 50)
# print(bulbasaur.health)
bulbasaur.print_info()
bulbasaur.level_up()
bulbasaur.print_info()