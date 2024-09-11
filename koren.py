def single_root_words(root_word, *other_words):
    my_list=[]
    for word in other_words :
        if  word.upper().find(root_word.upper())!=-1 or root_word.upper().find(word.upper())!=-1 :
            my_list.append(word)
    return my_list

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)