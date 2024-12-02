import inspect
from pprint import pprint

class MyObject:
    def __init__(self,name):
        self.name = name
        self.parameter1 = "Значение 1"
        self.parameter2 = "Значение 2"

#функция создающая список с параметрами obj
def introspection_info(obj):
    spisok={}
    spisok['module']=inspect.getmodule(obj) # Модуль, к которому объект принадлежит
    spisok['type']=type(obj)                # Тип объекта
    spisok['attributes']=vars(obj)          # Атрибуты объекта
    spisok['methods']= dir(obj)             # Методы объекта
    spisok['name object']=getattr(obj, "name") #вызовем атрибут name у объекта
    return spisok

#тестируем
my = MyObject("Мой объект")
number_info = introspection_info(my)
pprint(number_info)

