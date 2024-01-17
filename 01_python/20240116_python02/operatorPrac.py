print('' == True)
print('' == False)

if '' == True:               #빈 문자열은 if문에서는 False 판정
    print('빈문자열은 True')
else:
    print('빈문자열은 False')

three = ''
four = '4'
print(three and four)       # 얘는 빈문자열 출력

if three and four:
    print('3, 4')
else:
    print('실패')

one = 0
if one > 0 or one < 0:
    pass
if one != 0:
    pass
if one % 2 == 1:
    print('홀수')
else:
    print('짝수')
