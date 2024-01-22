# 아래 함수를 수정하시오.
def count_character(my_string, find_word):
    count = 0
    for s in my_string:
        if(s.find(find_word) != -1 ):
            count += 1
    return count

'''
def count_character(my_string, find_word):
    return word.count(find_word)
'''

result = count_character("Hello, World!", "o")
print(result)  # 2
