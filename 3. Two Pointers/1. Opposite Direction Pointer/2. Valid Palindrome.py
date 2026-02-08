    # Check if string is palindrome (ignoring non-alphanumeric)
    # Time: O(n), Space: O(1)

def ValidPalindrome(word):
    left,right=0,len(word)-1
    while left<right:
        while left<right and word[left].isalnum():
            left+=1
        while left<right and word[right].isalnum():
            right-=1

        if word[left].lower()!=word[right].lower():
            return False
        left+=1
        right-=1
    return True

#word="madam"
print(ValidPalindrome("A man, a plan, a canal: Panama"))  # True
print(ValidPalindrome("race a car"))  