#Рекурсивная функция
def get_multiplied_digits(number):
	str_number=str(number)
	if len(str_number)<=1:
		print("Последнее число: "+str_number)
		print('Начинаем умножение задом наперед')
		return number
	else :
		 first=int(str_number[0:1])
		 print('Отщепляем число: '+ str(first))
		 next=int(str_number[1:])
		 n=get_multiplied_digits(next)
		 print('Умножаем числа: '+str(n)+'*'+str(first)+'='+ str(n*first))
		 return n*first

#Проверка работы
numb=301257
print('Берем число: '+ str(numb))
print('Результат умножения чисел: '+str(get_multiplied_digits(numb)))