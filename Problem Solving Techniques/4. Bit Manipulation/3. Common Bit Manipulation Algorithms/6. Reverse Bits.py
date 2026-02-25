    # """Reverse bits of a 32-bit unsigned integer"""

def reverse_bits(n):
    result=0
    for i in range(32):
        bit= n&1
        result= (result<<1)|bit
        n>>=1
    
    return result
print(f"The orignal bit is {bin(13)[2:]}")
print(f"The Reverse bit is {bin(reverse_bits(13))[2:]}")
