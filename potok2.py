import threading as t
from time import sleep


class Knight(t.Thread):
	vragov=100
	
	def __init__(self,name,power):
		t.Thread.__init__(self)
		self.name=name
		self.power=power
	
	def run(self):
		day=0
		while self.vragov>0:
			day+=1
			#цикл для красоты
			for i in range(1,self.power):
				sleep(0.01)
			self.vragov-=self.power
			if day==1:
				print(f"{self.name} на нас напали!")
				sleep(0.5)
			print(f"{self.name} сражается {day} день(дня), осталось {self.vragov} воинов")
			sleep(1)
		print(f"{self.name}  одержал победу спустя {day} дней")
		

# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
		
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы окончены!")
