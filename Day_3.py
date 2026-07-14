# Find first character that doesn't repeat.

def non_repeat_char(s):
    
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
        
    for char in s:
        if(char_count[char] == 1):
            return char
    
    return None



print(non_repeat_char("hello numan what is new"))