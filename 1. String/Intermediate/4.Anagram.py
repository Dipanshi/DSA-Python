# Check if two strings are anagrams
s1 = input("Enter first string: ")
s2 = input("Enter Second string: ")
check = True
for i in s1:
    if i not in s2:
        print('Two strings are nor Anagrams.')
        check=False
        break
if check:
    print('Two strings are Anagrams.')
