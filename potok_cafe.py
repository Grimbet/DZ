from queue import Queue
import threading as t
from time import sleep
from random import randint


#стол
class Table:
	
	def __init__(self,number,guest=None):
		self.number= number
		self.guest=guest
	
	def __str__(self):
		return str(self.number)	
				
		
#гость
class Guest(t.Thread):
	
	def __init__(self,name):
		t.Thread.__init__(self)
		self.name= name
		
	def __str__(self):
		return self.name
		
	def run(self):
		pause = randint(3,10)
		sleep(pause)
		

#кафе()
class Cafe:
	q=Queue()
	
	def __init__(self,*tables):
		#список столов
		self.tables = tables
	
	# прием гостей	
	def guest_arrival(self,*guests):
		#список гостей
		self.guests=guests
		for g in self.guests:
			posadka=False
			for table in self.tables:
				if table.guest is None:
					g.start()
					print(f"{g} сел(а) за стол номер {table}")
					sleep(0.5)
					table.guest=g
					posadka=True
					break
			if posadka==False:
				print(f"{g} в очереди")
				sleep(0.5)
				self.q.put(g)	
					
	#обслуживание гостей
	def discuss_guests(self):
		posadka=True
		while posadka:
			posadka=False
			for table in self.tables:
				guest = table.guest
				#если хоть один стол занят
				if guest!=None:
					posadka = True
				#если поток завершен
				if guest!=None and guest.is_alive()==False:
					table.guest=None
					print(f"{guest} покушал(а) и ушёл(ушла)")
					print(f"Стол номер {table} свободен")
					sleep(2)
					if not self.q.empty():
						guest=self.q.get()
						print(f"{guest} вышел(вышла) из очереди и сел(а) за стол номер {table}")
						sleep(1)
						guest.start()
						table.guest=guest
						posadka=True
	
# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

print("Кафе открыто. Мы работаем до последнего клиента\n")
sleep(2)
# Заполнение кафе столами
cafe = Cafe(*tables)
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
print("\nВсе столы пусты. Клиентов нет. Кафе закрыто...")
