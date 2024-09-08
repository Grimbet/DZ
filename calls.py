calls = 0

#функция обновляет счетчик запусков функций
def count_calls():
    global calls    #объявляем глобальной, чтобы менялась
    calls+=1

#функция создает кортеж: длина, строка в нижнем регистре, строка в верхнем регистре
def string_info(my_str):
    count_calls() #обновляем счетчик запусков
    my_tuple=(str(len(my_str)),my_str.lower(),my_str.upper())
    return tuple(my_tuple)

#функция ищет слова string в списке list_to_search
#возвращает True, если нашла и False, если нет
#регистр букв игнорируется
def is_contains(string,list_to_search):
    count_calls() #обновляем счетчик запусков
    for i in range(0,len(list_to_search)) :
        if string.upper() == list_to_search[i].upper() : #игнорим регистр
            return True
    return False

#Запускаем 5 раз наши функции
print(string_info("Строка №1"))
print(string_info("Запуск 2"))
print(is_contains('3список', ['3 список', '3СписоК', 'Список №3'])) # Urban ~ urBAN
print(string_info("Попытка №4"))
print(is_contains('Список5', ['список 5', 'Пятый список'])) # No matches
#Проверяем счетчик, верно ли посчитал 5?
print("Мы запустили функции 'string_info' и 'is_contains' : "+str(calls)+" раз")