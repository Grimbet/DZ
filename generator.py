# функция ненератора
def all_variants(text):
    for k in range(1,len(text)+1):
    	for i in range(len(text)):
    	    if (i+k)<(len(text)+1):
            	yield text[i:i+k]
            	
a = all_variants("abc")
for i in a:
	print(i)

