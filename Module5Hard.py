from time import sleep


class Video:

    # инициализация класса
    def __init__(self,title:str, duration:int, time_now=0, adult_mode=False):
        # инициализация класса
        self.title = title
        self.duration=duration
        self.time_now=time_now
        self.adult_mode=adult_mode

    #равенство двух объектов класса Video
    def __eq__(self, other):
        if self.title == other.title:
            return True
        else:
            return False

    # ==============вывод вместо object==========================
    def __repr__(self):
        return f"<Title:{self.title};Sec:{self.duration};Start:{self.time_now};Dostup:{self.adult_mode}>"


class User:

    # инициализация класса
    def __init__(self,nickname:str, password:int, age:int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __repr__(self):
        return f"<Login:{self.nickname};Hash:{self.password};Age:{self.age}>"


class UrTube:

    users=[]
    videos=[]
    current_user="None"


    # ==============инициализация класса==========================
    def __init__(self):
        pass

    # ==============вывод вместо object==========================
    def __str__(self):
        return self.title

    #=====================вход пользователя========================
    def log_in(self,nickname:str,password:str):
        for log in self.users:
            if log.nickname == nickname and hash(password) == log.password :
                self.current_user=nickname
                break
            else:
                self.current_user = "None"


    #==========================сбросить пользователя==============
    def log_out(self):
        self.current_user = "None"


    #====================регистрация пользователя==================
    def register(self,nickname:str,password:str,age:int):
        user = User(nickname,hash(password),age)
        status_login = False
        for u in self.users:
            if u.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                status_login = True
                break
        # если нет такого в БД - регистрируем
        if status_login == False:
            self.users.append(user)
            # и логинимся сразу
            self.log_in(nickname, password)


    #==================добавление видео============================
    def add(self,*arg_video):
        for new_video in arg_video :
            if isinstance(new_video,Video):
                status_video = False
                for basa_video in self.videos:
                    if basa_video == new_video:
                        status_video = True
                if status_video==False:
                    self.videos.append(new_video)


    #===================================поиск по видео==============
    def get_videos(self,poisk:str):
        posik_list=[]
        for word in self.videos:
            if word.title.lower().find(poisk.lower())!=-1:
                posik_list.append(word.title)
        return posik_list

    #=======================просмотр видео==========================
    def watch_video(self,video):
        if self.current_user=="None":
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            status_video = True
            for u in self.users:
                if u.nickname==self.current_user and u.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    status_video = False
                    break
            if status_video ==True:
                status_basa = False
                for word in self.videos:
                    if word.title == video:
                        timer=0
                        while timer != word.duration:
                            timer+=1
                            print(timer,end=" ")
                            sleep(1)
                        print("Конец")
                        sleep(1)
                        status_basa = True
                        break
                if status_basa == False:
                    print(f"Видео с названием <{video}> не найдено")

def Spisok(*data):
    list=[]
    for my in data:
        list.append(my)
    return list


#ТЕСТИРОВАНИЕ

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 20)
v2 = Video('Для чего девушкам парень программист?', 5, adult_mode=True)


print(v1)

# Добавление видео
print("Добавили видео: ", v1.title)
print("Добавили видео: ", v2.title)
ur.add(v1, v2)
print("Список после добавления видео выглядит так:")
print(Spisok(ur.videos))
print("Попытаемся добавить видео повторно")
ur.add(v1)
print("Как видим - неудачно! ",Spisok(ur.videos))
# Проверка поиска
print("Попробуем найти все видео по поиску слова: <лучший>")
print(ur.get_videos('лучший'))
print("Попробуем найти все видео по поиску слова: <ПРОГ>")
print(ur.get_videos('ПРОГ'))


# Проверка на вход пользователя и возрастное ограничение
print("Попробуем посмотреть видео если мы не вошли в аккунт")
ur.watch_video('Для чего девушкам парень программист?') #Войдите в аккаунт
print("Регистрируем пользователя, которому 13 лет")
ur.register('vasya_pupkin', 'lolkekcheburek', 13)   #Вам нет 18 лет
print("Успешно")
print("Попробуем посмотреть видео, которое ограничено 18 лет!")
ur.watch_video('Для чего девушкам парень программист?') #
print("Регистрируем 25 летнего пользователя")
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
print("Попробуем запустить от его имени видео")
ur.watch_video('Для чего девушкам парень программист?')
print("Попробуем повторно зарегить уже зарегистрированного!")
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print("Выведем пользователя, который сейчас в аккаунте")
print(ur.current_user)
print("Попытка воспроизведения несуществующего видео")
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
print("Выйдем им из базы")
ur.log_out()

print("Подытожим...")
print("Наш список видео: ")
print(Spisok(ur.videos))
print("Наш список пользователей: ")
print(Spisok(ur.users))