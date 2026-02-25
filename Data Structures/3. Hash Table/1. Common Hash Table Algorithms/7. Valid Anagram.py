    # Check if two strings are anagrams
    # O(n) time, O(1) space
def is_anagram(s, t):
    """
    Check if two strings are anagrams
    O(n) time, O(1) space
    """
    if len(s) != len(t):
        return False
    
    char_count = {}
    
    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrease count for characters in t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True

from collections import Counter
def is_anagram_v2(s, t):
    return Counter(s)==Counter(t)


print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False
