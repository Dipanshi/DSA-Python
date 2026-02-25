# Implement a simple Caesar cipher encryption 
# It is a substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

word = input("Enter the word to encrypt: ")
result=''
shift=3
for ch in word:
    start= ord('A') if ch.isupper() else ord('a')
    result+= chr((ord(ch)-start + shift)%26 + start)

print(f'The word after encryption is {result}')


