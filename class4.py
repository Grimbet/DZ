class House:
    houses_history = []
    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    #инициализация класса
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    #попытка доехать на этаж new_floor
    def go_to(self, new_floor):
        print(self.name)
        print("Хотим на этаж: ", new_floor)
        if new_floor < 1:
            print("Этаж не может быть ниже 1")
            exit()
        for etag in range(1, new_floor + 1):
            if self.number_of_floors < etag:
                print("В данном доме нет этажа", etag, "и выше")
                break
            else:
                print("Мы на этаже: ", etag)

    #возвращает объект описание
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    #возвращает длину (кол-во этажей)
    def __len__(self):
        return self.number_of_floors
    #==
    def __eq__(self, other):
        if isinstance(other, House):
            if self.number_of_floors == other.number_of_floors :
                return True
            else :
                return False
    #<
    def __lt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors < other.number_of_floors :
                return True
            else :
                return False
    #<=
    def __le__(self, other):
        if isinstance(other, House):
            if self.number_of_floors <= other.number_of_floors :
                return True
            else :
                return False
    #>
    def __gt__(self, other):
        if isinstance(other, House):
            if self.number_of_floors > other.number_of_floors :
                return True
            else :
                return False
    #>=
    def __ge__(self, other):
        if isinstance(other, House):
            if self.number_of_floors >= other.number_of_floors :
                return True
            else :
                return False
    #!=
    def __ne__(self, other):
        if isinstance(other, House):
            if self.number_of_floors != other.number_of_floors :
                return True
            else :
                return False
    #замена оператора +
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors+value
            return self
    #замена оператора =+
    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors =+ value
            return self

    #замена оператора +=
    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __del__(self):
        print(self.name, "снесён, но он останется в истории")


h1 = House('ЖК Горский', 18)
print(House.houses_history)
h2 = House('ЖК Волна', 2)
print(House.houses_history)
h3 = House('ЖК Русь', 5)
print(House.houses_history)
# Удаление объектов
del h2
del h3

print(House.houses_history)



# h1.go_to(-5)
# h1.go_to(5)
# h2.go_to(10)
#print(h1)
#print(h2)
#print(len(h1))
#print(len(h2))

#print(h1) #Горский, этажность 18
#print(h2) #Волна, этажность 2
#h1 = h1 + 10 # __add__ добавим 10 этажей к 18
#print(h1)   #теперь этажность 28
#h1 += 10 # __iadd__
#print(h1) #теперь этажность 38
#h2 = 10 + h2 # __radd__
#print(h2) # у 2 дома теперь этажность 12


#перегрузка операторов
#print(len(h1),'==',len(h2),'>>', h1 == h2) #eq
#print(len(h1),'>',len(h2),'>>', h1 > h2) # __gt__
#print(len(h1),'>=',len(h2),'>>', h1 >= h2) # __ge__
#print(len(h1),'<',len(h2),'>>', h1 < h2) # __lt__
#print(len(h1),'<=',len(h2),'>>', h1 <=


