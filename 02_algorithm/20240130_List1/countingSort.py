arr = [0, 4, 1, 3, 1, 2 ,4 ,1]

# 1단계
# Data에서 각 항목들의 발생 회수를 세고, 
# 정수 항목들로 직접 인덱스 되는 카운트 배열counts에 저장한다.

# counts 배열 : 숫자를 세는 배열
# temp 배열 : 정렬된 숫자가 들어갈 배열
counts = [0] * (max(arr) + 1)
temp = [0] * len(arr)

# counts 배열로 어느 원소가 얼마나 나왔는지 셈
for i in arr:
    counts[i] += 1

# counts의 개수를 누적하여 원소를 조정
for i in range(1, len(counts)):
    counts[i] += counts[i-1]

# 카운트 배열을 통해 temp에 정렬된 숫자를 삽입
for i in range(len(arr)-1, -1, -1):
    counts[arr[i]] -= 1
    temp[counts[arr[i]]] = arr[i]

print(temp)