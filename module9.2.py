first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']
# вывести длины слов от 5 и выше из 1 списка
first_result=[len(s) for s in first_strings if len(s)>=5]

#вывести равные по буквам слова 2х списков
second_result=[ (x,y) for x in first_strings for y in second_strings if len(x)==len(y)]

#вывести словарь слово : кол.символов только емли четное кол оба списка
third_result={x: len(x) for x in (first_strings+second_strings) if len(x)%2==0}

print(first_result)
print(second_result)
print(third_result)
