#класс ошибки
class StepValueError(ValueError):
	def __init__(self):
		pass
	
class Iterator:
	
	def __init__(self, start, stop, step=1):
		self.start=start
		self.stop=stop
		self.step=step
		
	def __iter__(self):
		self.start-=self.step
		return self
		
	def __next__(self):
		if self.step==0:
			raise StepValueError
		self.start+=self.step	
		if (self.start>self.stop and self.step>0)or(self.start<self.stop and self.step<0):
			raise StopIteration()
		return self.start

#выдаст Шаг указан неверно
try:
	iter1 = Iterator(100, 200, 0)
	for i in iter1:
		print(i, end=' ')
except StepValueError:
	print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

#выдаст от -5 -4 -3 -2 -1 0 1
for i in iter2:
	print(i, end=' ')
print()	
#выдаст 6 8 10 12 14
for i in iter3:
	print(i, end=' ')
print()
#выдаст 5,4,3,2,1
for i in iter4:
	print(i, end=' ')
print()	
# ничего не даст, тк 10 выше 1 сразу
for i in iter5:
	print(i, end=' ')
print()
