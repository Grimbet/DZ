import multiprocessing
from multiprocessing.pool import Pool
import time

all_data=[]


def read_info(name):
    global all_data
    start = time.time()
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            # считываем строку
            line = file.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            # выводим строку
            all_data.append(line.strip())
    end = time.time()
    print(f"Считали файл {name} за {round(end - start,2)}с")

#создаем список файлов для чтения
filenames = [f'file {number}.txt' for number in range(1, 5)]

'''
#Линейный способ
start = time.time()
for name in filenames:
    read_info(name)
end = time.time()
print(f"Линейный способ занял у нас {round(end - start,2)}с")
'''

#Мнгопроцессынй способ
if __name__ == '__main__':
    start = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info,filenames)
    end = time.time()
    print(f"Многопроцессный способ занял у нас {round(end - start,2)}с")
