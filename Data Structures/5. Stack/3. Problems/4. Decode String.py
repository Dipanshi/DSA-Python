def decode_string(s):
    """
    Decode encoded string k[encoded_string]
    Time: O(n), Space: O(n)
    """
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_str, current_num))
            current_str = ""
            current_num = 0
        elif char == ']':
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char
    
    return current_str

# Test:
print(decode_string("3[a]2[bc]"))     # aaabcbc
print(decode_string("3[a2[c]]"))      # accaccacc
print(decode_string("2[abc]3[cd]ef")) # abcabccdcdcdef
print(decode_string("abc3[cd]ef")) # abcabccdcdcdef