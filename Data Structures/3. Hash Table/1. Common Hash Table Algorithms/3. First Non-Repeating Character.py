    # Find first character that appears only once
    # O(n) time, O(1) space (at most 26 letters)


def first_non_repeating_char(s):
    freq_index={}
    for c in s:
        freq_index[c]=freq_index.get(c,0)+1
    for c in s:
        if freq_index[c]==1:
            return c
    return -1

print(first_non_repeating_char("leetcode"))    # "l"
print(first_non_repeating_char("loveleetcode")) # "v"

from collections import Counter 
def first_non_repeating_char_v2(s):
    counter= Counter(s)
    for c in s:
        if counter[c]==1:
            return c
    return -1

print(first_non_repeating_char_v2("leetcode"))    # "l"
print(first_non_repeating_char_v2("loveleetcode")) # "v"
