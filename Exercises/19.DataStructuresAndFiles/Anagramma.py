import collections


def is_anagramma(word1, word2) -> bool:
    counter1 = collections.Counter(list(word1))
    counter2 = collections.Counter(list(word2))
    return counter1 == counter2


print(is_anagramma("aas", "aas"))
print(is_anagramma("das", "saa"))
anagramas = ["dad", "add", "lab", "aas", "bal"]

index = 0
for i in range(index, 5):
    for j in range(index + 1, 5):
        print(f"({i},{j})")
