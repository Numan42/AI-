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


# """Find missing number from 1 to n in O(n) time."""

def find_missing(nums):
    n = len(nums) + 1  # n-1 numbers given, find the nth
    expected_sum = n * (n + 1) // 2  # Sum of 1 to n
    actual_sum = sum(nums)
    return expected_sum - actual_sum