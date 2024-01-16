#변수를 사용하지 않고 출력

print(3 * 2)
print(3 ** 2)
print(3 ** 2 // (3 * 2), 3 ** 2 % (3 * 2))
print(3 ** 2 + (-3) ** 2)

print()

#변수를 사용하고 출력

answer_1 = 3 * 2
answer_2 = 3 ** 2
answer_3_1 = answer_2 // (answer_1)
answer_3_2 = answer_2 % (answer_1)
answer_4 = answer_2 + (-3) ** 2

print(answer_1)
print(answer_2)
print(answer_3_1, answer_3_2)
print(answer_4)