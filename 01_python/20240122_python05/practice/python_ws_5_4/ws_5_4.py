# 아래 함수를 수정하시오.
# def capitalize_words(my_string):
#     return my_string.title()


# 이렇게도 가능
def capitalize_words(word):
    result = ''
    temp = ''
    
    for index in range(len(word)):
        if index == 0 or temp == ' ':
            result += word[index].upper()
        else:
            result += word[index]
        temp = word[index]
    return result


result = capitalize_words("hello, world!")
print(result)
