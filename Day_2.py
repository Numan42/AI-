# "Return the string"
def reverse_string(str):
    result = ""
    for char in str:
        result = char + result
    return result

# print(reverse_string("hello"))

"Check for Palindrome"
def is_Palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned == cleaned[::-1]

print(is_Palindrome("A man a plan a canal Panama"))
# "solve two question today"
