#Исходные данные
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#Задача : выписывать из этого списка только положительные числа до тех пор,
# пока не встретите отрицательное или не закончится список
k = 0 #Стартуем с 1 символа списка
while len(my_list) > k : #выполняем цикл пока не достигнем конца списка
    numb=int(my_list[k])
    if numb > 0 :
        if numb == 0 :
            continue
        print(numb)
    if numb < 0 :
        break
    k += 1  # двигаемся на символ дальше