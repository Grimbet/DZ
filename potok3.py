import threading as t
from random import randint
from time import sleep



class Bank:
	balance=0
	lock=t.Lock()
	sleep=0.1
	
	def __init__(self):
		pass
	
	def deposit(self):
		for i in range(1,101):
			self.lock.acquire()
			money=randint(50,500)
			self.balance +=money
			print(f"{i}: Пополнение: {money}\u20BD. Баланс: {self.balance}\u20BD")
			self.lock.release()
			sleep(self.sleep)
			
	
	def take(self):
		
		for i in range(1,101):
			self.lock.acquire()
			money=randint(50,500)
			print(f"Запрос на снятие {money}\u20BD")
			if self.balance<money:
				print(f"{i}: Запрос отклонён, недостаточно средств..." )
				self.lock.release()
				sleep(self.sleep)
				
			else:
				self.balance -= money
				print(f"{i}: Снятие: {money}\u20BD. Баланс: {self.balance}\u20BD")
				self.lock.release()
				sleep(self.sleep)
		
				
	
		
bk=Bank()

th1 = t.Thread(target=Bank.deposit, args=(bk,))
th2 = t.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'\nИтоговый баланс: {bk.balance}\u20BD')

