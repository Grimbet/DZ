import threading as t
from time import sleep,time

def write_words(word_count, file_name):
	file = open(file_name,'w',encoding='utf-8')
	start= time()
	for num in range(word_count):
		file.write(f"Какое-то слово №{num}\n")
		sleep(0.1)
	fin = time()
	file.close
	print(f"Завершилась запись в файл {file_name} time: {round(fin-start,2)} c")

#function
st=time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end=time()
print(f"\nОбщая работа функций: {end-st}\n")

#thread
t1=t.Thread(target=write_words,args=(10, 'example1.txt'))
t2=t.Thread(target=write_words,args=(30, 'example2.txt'))
t3=t.Thread(target=write_words,args=(200, 'example3.txt'))
t4=t.Thread(target=write_words,args=(100, 'example4.txt'))

st=time()
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

end=time()
print(f"\nОбщая работа потоков {end-st}\n")
