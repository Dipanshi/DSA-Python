def is_odd(n):
    """Check if least significant bit is 1"""
    return (n&1)==1

def is_even(n):
    """Check if least significant bit is 0"""
    return (n&1)==0


print(is_odd(2))
print(is_odd(3))
print(is_even(4))
print(is_even(9))

