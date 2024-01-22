def restructure_word(word, arr):
    for c in word:
        if c.isdecimal():
            for i in range(int(c)):
                arr.pop()
        else:
            arr.remove(c)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

arr.extend(original_word)


result = restructure_word(word, arr)
result = ''.join(result)
print(result)
