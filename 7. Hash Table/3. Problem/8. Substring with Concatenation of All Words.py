from collections import Counter

def find_substring_concatenation(s, words):
    """
    Find all starting indices where substring is concatenation of all words
    O(n * m * k) time where n=len(s), m=len(words), k=len(words[0])
    """
    if not s or not words:
        return []
    
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_freq = Counter(words)
    result = []
    
    for i in range(len(s) - total_len + 1):
        seen = {}
        j = 0
        
        while j < word_count:
            word_start = i + j * word_len
            word = s[word_start:word_start + word_len]
            
            if word not in word_freq:
                break
            
            seen[word] = seen.get(word, 0) + 1
            
            if seen[word] > word_freq[word]:
                break
            
            j += 1
        
        if j == word_count:
            result.append(i)
    
    return result

# Test:
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(find_substring_concatenation(s, words))  # [0, 9]