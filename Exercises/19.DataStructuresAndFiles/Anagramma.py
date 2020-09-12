import collections


def is_anagramma(word1, word2) -> bool:
    counter1 = collections.Counter(list(word1))
    counter2 = collections.Counter(list(word2))
    return counter1 == counter2


anagrams = ["dad", "add", "lab", "aas", "bal", "dda"]
anagrams_dics = {word: collections.Counter(list(word)) for word in anagrams}

dic_found = {}


def foo(ang_dict):
    index = 0
    for dic1_k, dic1_v in ang_dict.items():
        print(f"----> Cycle {index}")
        for dic2_k, dic2_v in ang_dict.items():
            if dic1_v == dic2_v:
                print(f"FOUND $${dic1_k},{dic2_k}$$")
            else:
                print(f"{dic1_k},{dic2_k}")
        index += 1


foo(anagrams_dics)
