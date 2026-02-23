def simplify_path(path):
    """
    Simplify Unix file path
    Time: O(n), Space: O(n)
    """
    stack = []
    
    for part in path.split('/'):
        if part == '..' and stack:
            stack.pop()
        elif part and part != '.' and part != '..':
            stack.append(part)
    
    return '/' + '/'.join(stack)

# Test:
print(simplify_path("/home/"))           # /home
print(simplify_path("/../"))             # /
print(simplify_path("/home//foo/"))      # /home/foo
print(simplify_path("/a/./b/../../c/"))  # /c