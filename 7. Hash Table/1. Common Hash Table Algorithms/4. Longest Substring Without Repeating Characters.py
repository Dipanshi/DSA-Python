    # Find length of longest substring without repeating chars
    # O(n) time, O(min(m, n)) space where m = charset size

def longest_substring_without_repeating(s):
    left=0
    word_dict={}
    max_lenght=0
    for right,c in enumerate(s):
        if c in word_dict and word_dict[c]>=left:
            left=word_dict[c]+1
        word_dict[c]=right
        max_lenght=max(max_lenght,right-left+1)
    return max_lenght

print(longest_substring_without_repeating("abcabcbb"))
print(longest_substring_without_repeating("bbbbb"))
print(longest_substring_without_repeating("pwwkew"))



