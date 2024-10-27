def add_everything_up(a, b):
    try:
        rez = a + b
    except TypeError:
        rez = str(a)+str(b)
    return rez

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.451, 7))
