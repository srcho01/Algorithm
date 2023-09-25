def error(s):
    if s[-1] == '_' or s[0] == '_' or "__" in s or s[0].isupper():
        print("Error!")
        return True
    if '_' in s and s != s.lower():
        print("Error!")
        return True
    return False

def change_variable(s):
    if error(s): return

    if '_' in s: # C++ Style
        s = s.split('_')
        print(s[0], end='')
        for w in s[1:]:
            print(w[0].upper() + w[1:], end='')
    else: # Java Style
        for c in s:
            if c.islower():
                print(c, end='')
            else:
                print(f"_{c.lower()}", end='')

s = input().rstrip()
change_variable(s)