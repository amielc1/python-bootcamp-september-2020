import collections


def is_anagramma(word1, word2) -> bool:
    counter1 = collections.Counter(list(word1))
    counter2 = collections.Counter(list(word2))
    return counter1 == counter2


print(is_anagramma("aas", "aas"))
print(is_anagramma("das", "saa"))
anagramas = ["dad", "add", "lab", "aas", "bal"]
# anagramas_dic = {}
# for word in anagramas:
#     anagramas_dic[word]=collections.Counter(word)
# for i in range(anagramas_dic):
#     if

# for i in range(anagramas)-1:
#     if is_anagramma(anagramas[i],anagramas[i+1]):

# dad
# add
# lab
# aas
# bal
