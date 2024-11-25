import requests
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#requets
#с помощью библиотеки можно качать файлы с интернета
#проверять подключение, отправляь get и Post запросы и др

#создал функцию по скачиванию файлов из интернета
def download_file(url:str,filename:str):
    r = requests.get(url)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(r.content)
            print(f"Файл {url} успешно сохранен!")
    else:
        print(f"Неудачное соединение с {url}")


#Качаем картинку из интернета
download_file("https://i.pinimg.com/736x/a7/44/f4/a744f4a8d41c5e6cca3d476b4ed49fe2.jpg","my_picture.jpg")
#Скачаем русский шрифт
download_file("https://github.com/kavin808/arial.ttf/blob/master/arial.ttf","arial.ttf")

#Применим pillow (PIL) - эта библиотека позволяет рисовать, работать с графикой и многое другое
#дает кучу возможностей работы с изображениями
img = Image.open('my_picture.jpg') #откроем наш скаченный файл
font = ImageFont.truetype("arial.ttf", size=25) #объект нашего шрифта
idraw = ImageDraw.Draw(img) #объект канвы
idraw.text((15, 5), 'Я учусь в Urban University!',font=font) #делаем надпись на картинке
img.save('my_picture.jpg') #сохраним результат
img.show() #покажем наш результат




