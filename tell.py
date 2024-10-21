def custom_write(file_name, strings):
        mydict={}
        file = open(file_name, 'w', encoding='utf-8')  # создаем файл, не забываем про кодировку
        num_str=0
        for str in strings:
            str_byte = file.tell()       # запоминаем позицию курсора
            num_str+=1                   # узнаем номер строки
            mydict[num_str,str_byte]=str # выводим в словарь
            file.write(str+'\n')         # записываем строку в файл
        file.close()                     # закрываем файл
        return mydict

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)