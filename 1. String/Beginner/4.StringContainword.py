# Check if a string contains a specific word

s = input('Enter the sentence you want to search in :')
word = input('Enter the word you want to search : ')
if word in s:
    print('Sentence contain the word!!')
else:
    print("Sentence doesn't contain word!!")
    