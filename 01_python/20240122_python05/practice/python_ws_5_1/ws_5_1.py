# 아래 함수를 수정하시오.
def reverse_string(string):
    reverse = ''.join(reversed(string))
    return reverse


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
