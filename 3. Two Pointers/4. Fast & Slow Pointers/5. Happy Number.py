#  Determine if number is happy
#   Time: O(log n), Space: O(1)

def HappyNumber(N):

    def get_num(N):
        total=0
        while N>0:
            digit= N%10
            total += digit*digit
            N//=10
        return total
    
    slow=N
    fast=get_num(N)

    while fast!=1 and slow!=fast:
        slow=get_num(slow)
        fast=get_num(get_num(fast))
    
    return fast==1

print(HappyNumber(19))  # True
print(HappyNumber(2))   # False

