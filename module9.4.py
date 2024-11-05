from random import choice

#Lambda
print('<Lambda>\n')
first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x,y: x==y, first, second)))

#Замыкание
def get_advanced_writer(file_name):
	if type(file_name)==str:
		def write_everything(*data_set):
			with open(file_name,'w') as f:
				for char in data_set:
					f.write(str(char)+'\n')
			print('Файл <' + file_name+'> имеет вид:')
			with open(file_name,'r') as ff:	
				print(ff.read())
	return write_everything
	
#проверка работы замыкания
print('\n<Замыкание>\n')
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__
#создаем класс
class MysticBall:
		
		def __init__(self,*words):
			self.words = words
			
		def __call__(self):
			return choice(self.words)
		
#варианты ответов						
first_ball = MysticBall('Да', 'Нет', 'Наверное','Вероятность 30%','Можно,если осторожно','Пополам','20 на 80')

print('<Метод __call__>\n')
print(first_ball())
print(first_ball())
print(first_ball())	