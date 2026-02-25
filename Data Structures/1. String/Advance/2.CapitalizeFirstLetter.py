# Create a function that capitalizes the first letter of each word
#Method 1
# def capitalize(s):
#     res=s.title()
#     return res

# if __name__=="__main__":
#     print(capitalize(input("Enter the string")))

#Method 2
def capitalize(s):
    s_list= s.split(' ')
    for i in range(len(s_list)):
        s_list[i]= s_list[i].replace(s_list[i][0],s_list[i][0].upper())
    return " ".join(s_list)

if __name__=="__main__":
    print(capitalize(input("Enter the string : ")))

