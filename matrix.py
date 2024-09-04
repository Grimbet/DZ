def get_matrix(n,m,value):
    matrix=[]   #создаем пустой список
    for i in range(0,n):    #начинаем перебор по столбцам
        stroka=[]
        for j in range(0,m): #начинаем перебор по строкам
            stroka.append(value) #формируем строку из n элементов value
        matrix.append(stroka)   #добавляем список в матрицу
    return matrix   #выводим

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

