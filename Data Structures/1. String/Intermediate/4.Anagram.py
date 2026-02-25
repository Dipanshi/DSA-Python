# Check if two strings are anagrams
s1 = input("Enter first string: ")
s2 = input("Enter Second string: ")
# check = True
# for i in s1:
#     if i not in s2:
#         print('Two strings are not Anagrams.')
#         check=False
#         break
# if check:
#     print('Two strings are Anagrams.')

#Method 2
s1_set=set(s1)
s2_set=set(s2)
if s1_set==s2_set:
    print('Two strings are Anagrams.')
else:
    print('Two strings are not Anagrams.')