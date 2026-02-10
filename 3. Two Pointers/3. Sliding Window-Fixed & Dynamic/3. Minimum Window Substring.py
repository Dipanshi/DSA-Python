    # Find minimum window in s containing all characters of t
    # Time: O(n + m), Space: O(m)

from collections import Counter

def min_window_substring(s, t):
    if not s or not t:
        return None
    
    target_count= Counter(t)
    required=len(target_count)
    former=0
    word_count={}
    left=0
    result=(float('inf'),0,0)
    # step 1: add character to dict
    for right,char in enumerate(s):
        word_count[char]= word_count.get(char,0)+1
    #Step 2: if character in target and count is equal then increase former
        if char in target_count and target_count[char]==word_count[char]:
            former+=1
    # Step 3 : when substring found reduct to get miniumn substring
        while left<=right and former==required:
            if right-left+1<result[0]:
                result=(right-left+1,left,right)

            c=s[left]
            word_count[c]-=1
            if c in target_count and word_count[c]<target_count[c]:
                former-=1
            left+=1
    
    return "" if result[0]==float('inf') else s[result[1]:result[2]+1]

print(min_window_substring("ADOBECODEBANC", "ABC"))  # "BANC"

