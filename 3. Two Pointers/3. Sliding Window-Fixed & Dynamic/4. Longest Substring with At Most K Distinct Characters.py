    # Find longest substring with at most k distinct characters
    # Time: O(n), Space: O(k)

def longest_substring_k_distinct(s, k):
    if not s and k<=0:
        return 0
    s_set={}
    left=0
    max_len=0
    for right,char in enumerate(s):
        s_set[char]=s_set.get(char,0)+1
        while left<=right and  len(s_set)>k:
            c=s[left]
            s_set[c]-=1
            if s_set[c]==0:
                del s_set[c]
            left+=1
    
        max_len= max(max_len,right-left+1)
    return max_len


#String = "eceebacdeba"
print(longest_substring_k_distinct("eceebacdeba",2))
