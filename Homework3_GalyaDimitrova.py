#zadacha1
def is_anagram(fst_word, snd_word):
    fst_word = fst_word.upper()
    snd_word = snd_word.upper()

    if(len(fst_word) == len(snd_word)):
        sorted_fst = sorted(fst_word)
        sorted_snd = sorted(snd_word)
        
        if(sorted_fst == sorted_snd):
            return True
        else:
            return False

print(is_anagram("race","care"))
print(is_anagram("LISTEN","silent"))
print(is_anagram("BRADE","BeaRD"))
print(is_anagram("TOP_CORDER","COTO_PRODE"))


#zadacha2
print("primer2")
def count_words(arr):
    word_dic = {}
    for i in arr:
        if i not in word_dic:
            word_dic[i]=1
        else:
            word_dic[i]+=1
    return word_dic
print(count_words(["apple","apple","banana","pie"]))
print(count_words(["python","python","python","ruby"]))

#zadacha3
print("primer 3")
def nan_expand(num):
    word=" "
    if num == 0:
        return ' " " '
    for i in range(num):
        word+="not a "
    word+="nan "
    return word
    
print(nan_expand(2))
print(nan_expand(3))
print(nan_expand(0))

#zadacha 5
print("primer 5")
def sum_of_numbers(st):
    num = 0
    sum = 0
    for i in st:
        if i.isdigit():
            num = num*10+int(i)
        else:
            sum = sum+num
            num = 0
    return sum+num
print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("WELL12536ISTHISWORK9875"))



        


   




