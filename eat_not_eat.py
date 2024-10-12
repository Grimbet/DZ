class Animal:

    def __init__(self,name:str, alive = True, fed = False):
        self.alive = alive #живой или неживой
        self.fed = fed #сытый или голодный
        self.name = name

    def eat(self,food):
        if food.edible==True:
            print(f"<{self.name}> съел <{food.name}>")
            self.fed = True
        else:
            print(f"<{self.name}> не стал есть <{food.name}>")
            self.alive = False

class Plant:

    def __init__(self,name:str, edible = False):
        self.edible = edible #съедобный - True, несъедобный = False
        self.name = name




class Mammal(Animal):
    pass

class Predator(Animal):
    pass


class Flower(Plant):
    pass

class Fruit(Plant):

    def __init__(self,name:str, edible = True):
        self.edible = edible #все фрукты съедобные
        self.name = name




a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(f"{a1.name} жив? >> {a1.alive}")
print(f"{a2.name} сытый? >> {a2.fed}")
a1.eat(p1)
a2.eat(p2)
print(f"{a1.name} жив? >> {a1.alive}")
print(f"{a2.name} сытый? >> {a2.fed}")