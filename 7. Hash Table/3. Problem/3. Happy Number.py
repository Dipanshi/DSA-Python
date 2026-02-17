    # Determine if number is happy (sum of squares leads to 1)
    # O(log n) time, O(log n) space

def is_happy(n):
    sum_dic=set()
    while n!=1:
        num=n
        total=0
        while num>0:
            digit=num%10
            total+=digit**2
            num=num//10
        if total in sum_dic:
            return False
        else:
            sum_dic.add(total)
        n=total
    return True    

print(is_happy(19))
print(is_happy(2))

