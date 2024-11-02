'''
Генераторные сборки
'''
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

#формируем список разницы между строками списков при их разной длине
first_result=(len(x[0])-len(x[1]) for x in zip(first,second) if len(x[0])!=len(x[1]))

#формируем без zip список результатов сравнения длин строк двух списков
second_result=(len(first[i])==len(second[i])for i in range(len(first)))


print(list(first_result))
print(list(second_result))
