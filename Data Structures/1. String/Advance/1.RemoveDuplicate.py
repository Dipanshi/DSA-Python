# Write a function to remove all duplicates from a string

def remove_duplicate(s):
    res=''
    for i in s:
        if i not in res:
            res += i
    return res

if __name__ == "__main__":
    print(f'The upadtes string after removing duplicates is {remove_duplicate( input("Enter the string: "))}.')


