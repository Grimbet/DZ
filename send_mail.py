#Функция проверки email
def ProverkaText(email):
    if (email[-4:len(email)] == ".com" or email[-4:len(email)] == ".net" or email[-3:len(email)] == ".ru") and email.find('@')!=-1 :
        return True
    return False

#Функция обработки писем
def send_email(message, recipient, sender = "university.help@gmail.com"):
    if ProverkaText(recipient)==False or ProverkaText(sender)==False :
        print("Невозможно отправить письмо с адреса "+sender+" на адрес "+recipient)
    elif recipient==sender :
        print("Нельзя отправить письмо самому себе!")
    elif sender=='university.help@gmail.com':
        print("Письмо успешно отправлено с адреса "+sender+" на адрес "+recipient)
    else: print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "+sender+" на адрес "+recipient)

#Тестирование
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')