def calculate_structure_sum(basa):
    n = 0
    tip = type(basa)
    if tip == str or tip == int:
        if tip == str:
            val = len(basa)
        else :
            val = basa
        return val
    else:
        if tip == tuple or tip == list or tip==set :
            for item in basa:
                n = n + calculate_structure_sum(item)
        if tip == dict:
            for key, value in basa.items():
                n = n + calculate_structure_sum(key) + calculate_structure_sum(value)
        return n

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print("Итоговое число: "+str(result))
