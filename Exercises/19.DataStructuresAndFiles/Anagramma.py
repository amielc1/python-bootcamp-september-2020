import collections


def is_anagramma(word1, word2):
    counter1 = collections.Counter(list(word1))
    counter2 = collections.Counter(list(word2))
    print(counter1)
    print(counter2)
    if counter1.__eq__(counter2):
        print("counters equals")
    else:
        print("counters not equals")

is_anagramma("aas", "saa")
list = ["aas", "saa", "ffo""off"]

list = ["1", "2", 4.0, "3"]
print(max(map(float, list)))

#     1 add
#     2 dad
#     3 help
#     4 more
#     5 rome
#
# 12 13 14 15
# 21 23 24 25
# 31 32 24 35
