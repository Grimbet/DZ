#класс файлов
class WordsFinder:
	#список названий файлов
	file_names=[]
	#инициализация	
	def __init__(self, *files):
		self.files= files
		for f in files:
			self.file_names.append(f)
			
	#функция убирает знаки препинания
	def zamena(self,slovo):
			L=[',',' - ', '.', '!', '?',':',';','*']
			for symb in L:
				slovo = slovo.replace(symb,' ')	
			return slovo.split()
			
	#вывод словаря в виде {файл1:[слово1,слово2...],файл2:...}	
	def get_all_words(self):
		basa={}
		for file_name in self.file_names:
			with open(file_name, encoding='utf-8') as file:
				for line in file:
					list =self.zamena(line)			
				basa[file_name]=list
			return basa
			
	#поиск слова в тексте,выведет его  номер в списке при обнаружении
	def find(self,poisk):
		word=0
		sl=self.get_all_words()
		for value in sl.values():
			sp=value
			for i in range(1,len(value)):
				if poisk.lower()==sp[i].lower():
					word=i+1
					break
		return word
		
	#подсчитает кол-во слов в тексте
	def count(self,poisk):
		kol=0
		sl=self.get_all_words()
		for value in sl.values():
			for word in value:
				if poisk.lower()==word.lower():
					kol+=1
		return kol
				
#создадим файл  test_text.txt
text="It's a text for task! Чтобы найти его - используйте для самопроверки нужные схемы, верное решение задачи. text text text"
file=open('test_text.txt','w',encoding='utf-8')
file.write(text)
file.close()

#создадим объект
finder = WordsFinder('test_text.txt')

print(finder.get_all_words()) # Все слова
print(finder.find('TeXt')) # 3 слово по счёту
print(finder.count('teXT')) # 4 слова teXT в тексте всего
