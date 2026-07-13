# "Return the string"
def reverse_string(str):
    result = ""
    for char in str:
        result = char + result
    return result
