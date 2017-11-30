word_list = ['hello','world','my','name','is','Anna']
char="o"
new_list=[]


#for word in word_list:
    #if "o" in word:
        #new_list.append(word)
#print new_list


#The above method works also. But, below it works in a function.
def find_char(my_word_list,char):
    new_list = []
    for word in my_word_list:
        if char in word:
            new_list.append(word)
    return (new_list)


print (find_char(word_list,char))
