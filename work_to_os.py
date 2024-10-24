import os,time

#создадим директорию, если есть, то просто туда перейдем
if os.path.exists('directory'):
    os.chdir('directory')
else:
    os.mkdir('directory')
    os.chdir('directory')
#перейдем в нашу созданную директорию, запомним путь
directory=os.getcwd()
print("Путь к нашей директории:", directory)
#создадим два тестовых файла с разным расширением и размером
file1 = open('file1.txt','w')
file1.write('Это наш первый файл')
file1.close()
file2 = open('file2.doc','w')
file2.write('Это наш второй файл. Размер у него должен быть побольше!')
file2.close()

#перебираем нашу тестовую папку и наши созданные файлы
for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(directory,file)
    filetime = os.path.getmtime(file)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(file)
    parent_dir = os.path.dirname(directory)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

print('Работа с файлами освоена и закончена!')