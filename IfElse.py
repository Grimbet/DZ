first=input("Введите число: ")
second=input("Введите число: ")
third=input("Введите число: ")
f=int(first)
s=int(second)
t=int(third)

if f==s and t==s :
    print("Вы ввели 3 одинаковых числа")
elif (f==s or f==t or t==s)and(f!=s or s!=t or f!=t) :
    print("Вы ввели 2 одинаковых числа")
else :
    print("Вы ввели три разных числа")

