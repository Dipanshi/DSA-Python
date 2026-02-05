# Write a program to find the longest word in a sentence
sentence = input("Enter the sentence to check the longest word: ")
words = sentence.split(" ")
word=''
for w in words:
    if len(word)<len(w):
        word=w

print(f"The word with longest lenght is : {word}")