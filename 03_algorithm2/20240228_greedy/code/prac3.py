'''
각 학생 화장실 이용시간은 다음과 같다
time = {'A' : 15, 'B' : 30, 'C' : 50, 'D' : 10}
A가 사용한다면 각자 대기시간의 총 합은 45분이다
이후 B가 사용한다면 각자 대기시간의 누적합은 45 + 60 = 105분이다

대기시간의 누적합이 최소를 구해라
'''

time = [15, 30, 50, 10]
time.sort()
n = len(time)

result = 0
for i in range(n):
    for j in range(i+1, n):
        result += time[i]

print(result)


###########

sum = 0
left_person = n-1
for turn in range(n):
    temp = time[turn]
    sum += left_person * temp
    left_person -= 1
print(sum)