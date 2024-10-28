class Car:

    def __init__(self,model,__vin,__numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        #вызываем проверку vin и numbers
        self.__is_valid_numbers(self.__numbers)
        self.__is_valid_vin(self.__vin)

    #проверка на корректность vin_number
    def __is_valid_vin(self,vin_number):
        if type(vin_number)!=int:
            raise IncorrectVinNumber(f"{self.model} : Некорректный тип vin номер")
        if vin_number>100000 and vin_number<9999999:
            raise IncorrectVinNumber(f"{self.model} : Неверный диапазон для vin номера")
        return True

    # проверка на корректность numbers
    def __is_valid_numbers(self,numbers):
        if type(numbers)!=str:
            raise IncorrectVinNumber(f"{self.model} : Некорректный тип данных для номеров")
        if len(numbers)!=6:
            raise IncorrectVinNumber(f"{self.model} : Неверная длина номера")
        return True

#исключение по vin_number
class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message

#исключение по numbers
class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message

#Тестирование
try:
  first = Car('Model1', 300, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} : Успешно создана')

try:
  second = Car('Model2', 1000000, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} : Успешно создана')


try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} : Успешно создана')

