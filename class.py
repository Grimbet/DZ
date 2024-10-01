class House:
	
	def __init__(self,name,number_of_floors):
		self.name=name
		self.number_of_floors=number_of_floors
		print()
		print( "Мы в доме ",self.name)
			
	def  go_to(self,new_floor):
		print()
		print("Хотим на этаж: ",new_floor)
		if new_floor<1:
			 print("Этаж не может быть ниже 1")
			 exit
	
		for etag in range(1,new_floor+1):
			if self.number_of_floors<etag :
					print("В данном доме нет этажа",etag, "и выше")
					break
			else:
				print("Мы на этаже: ",etag)	
			

	def info(self):
		print("Название дома: #",self.name)
		print("Этажей: ",self.number_of_floors)
		
		
h1 = House('ЖК Горский', 18)
h1.go_to(-5)
h1.go_to(5)

h2 = House('ЖК Волна', 2)
h2.go_to(10)
