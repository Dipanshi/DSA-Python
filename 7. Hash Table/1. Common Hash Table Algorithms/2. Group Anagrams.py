    # Group words that are anagrams
    # O(n * k log k) time where k = max word length

def group_anagrams(words):
    res={}
    for word in words:
        word_set=''.join(sorted(word))
        if word_set in res:
            res[word_set].append(word)
        else:
            res[word_set]=[word]

    return list(res.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

