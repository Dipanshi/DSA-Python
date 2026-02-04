# Replace all vowels in a string with '*'
s = input('Enter the string which need replacement : ')
vowels=('a','e','i','o','u')
res= "".join("*" if c.lower() in vowels else c for c in s)
print(f'The update string is {res}')
