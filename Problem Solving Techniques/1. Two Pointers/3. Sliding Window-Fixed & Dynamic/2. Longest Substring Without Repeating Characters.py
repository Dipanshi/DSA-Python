    # Find length of longest substring without repeating characters
    # Time: O(n), Space: O(min(m, n)) where m = charset size

def length_of_longest_substring(s):
    left=0
    max_lenght=0
    char_index={}
    for right,char in enumerate(s):
        if char in char_index and right>char_index[char]:
            left=char_index[char]+1
        
        char_index[char]=right
        max_lenght=max(max_lenght,right-left+1)

    return max_lenght
    
print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # 1 ("b")
print(length_of_longest_substring("pwwkew"))    # 3 ("wke")
