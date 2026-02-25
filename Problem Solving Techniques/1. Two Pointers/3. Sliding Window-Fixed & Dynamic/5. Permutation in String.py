    # Check if s2 contains permutation of s1
    # Time: O(n), Space: O(1) - at most 26 characters
from collections import Counter

def check_inclusion(s1, s2):
    if len(s1)>len(s2):
        return False
    
    s1_counter=Counter(s1)
    word_counter= Counter(s2[:len(s1)])

    if s1_counter==word_counter:
        return True
    
    for i in range(len(s1),len(s2)):
        word_counter[s2[i]]=word_counter.get(s2[i],0)+1

        c=s2[i-len(s1)]
        word_counter[c]-=1
        if word_counter[c]==0:
            del word_counter[c]
        
        if s1_counter==word_counter:
            return True
        
    return False

print(check_inclusion("ab", "eidbaooo"))  # True
print(check_inclusion("ab", "eidboaoo"))  # False
        