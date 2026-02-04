# Reverse a string without using slicing

s = input('Enter the string you want to reverse: ')
r=[]
for i in range(len(s)-1,-1,-1):
    r +=s[i]

print(f'The reverse string is {"".join(r)}')