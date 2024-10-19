import os.path

#класс продукт
class Product:

    def __init__(self,name,weight,category):
        self.name= name
        self.weight = weight
        self.category = category

    #выводим строкой продукт
    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

#класс магазин
class Shop:
    __file_name = 'product_basa.txt'

    #открываем файл базы продуктов и выводим списком
    def get_products(self):
        L=[]
        #проверяем наличие файла - если нет - создаем
        if os.path.isfile(self.__file_name):
            file = open(self.__file_name,'r')
        else:
            file = open(self.__file_name, 'w')
            file = open(self.__file_name, 'r')
        L=file.readlines()
        file.close()
        return L

    #добавление нового продукта в магазин
    def add(self, *products):
        L = self.get_products()   #считаем файл
        for pro in products:
            poisk = False
            for line in L:
                str = line.strip()
                name=str[0:str.find(',')]
                if str.find(pro.name)!=-1 :
                    poisk = True
            if poisk == False:
                #если нет такого продукта
                new_pro=f"{pro.name}, {pro.weight}, {pro.category}\n"
                file = open(self.__file_name,'a')
                file.write(new_pro)
                file.close()
            else:
                print(f"Продукт <{pro.name}> уже есть в базе...")

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Tomato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())