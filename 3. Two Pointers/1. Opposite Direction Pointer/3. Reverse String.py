    # Reverse string in-place
    # Time: O(n), Space: O(1)
def ReverseString(word):
    left,right=0,len(word)-1
    word_list=list(word)
    while left<right:
        word_list[left],word_list[right]=word_list[right],word_list[left]
        left+=1
        right-=1
    return "".join(word_list)

word="life is beautiful"
print(ReverseString(word))
