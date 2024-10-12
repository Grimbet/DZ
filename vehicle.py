class Vehile:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self,owner,model,color,engine_power):
        self.owner=owner
        self.__model=model
        self.__engine_power=engine_power
        self.__color=color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"


    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print("Владелец: ",self.owner)

    def set_color(self,new_color:str):
        status_color=False
        for cvet in self.__COLOR_VARIANTS:
            if cvet.lower() == new_color.lower():
                self.__color=cvet
                status_color = True
        if status_color == False:
            print(f"К сожалению, нельзя сменить цвет на {new_color} т.к. его нет в базе цветов")


class Sedan(Vehile):

    __PASSENGERS_LIMIT = 5 #помещается 5 пассажиров



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
# Изначальные свойства
vehicle1.print_info()


# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
