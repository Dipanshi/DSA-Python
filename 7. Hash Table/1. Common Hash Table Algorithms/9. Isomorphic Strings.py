    # Check if strings are isomorphic (one-to-one mapping)
    # O(n) time, O(1) space (at most 256 chars)

def is_isomorphic(s, t):
    word_dict={}
    if len(s)!=len(t):
        return False
    for i,c in enumerate(s):
        if c in word_dict:
            if word_dict[c]!=t[i]:
                return False
        else:
            word_dict[c]=t[i]
    return True

    
print(is_isomorphic("paper","title")) #True
print(is_isomorphic("foo","bar")) # False
print(is_isomorphic("egg","add")) #True
