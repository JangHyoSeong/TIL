def bubblesort(numbers):

    for i in range(len(numbers)-1, 0, -1):   # for i : N-1 -> 1
        for j in range(i):    # for j:0 -> i

            if numbers[j]>numbers[j+1]:       # 왼쪽이 더 크면
                temp = numbers[j]           # 자리를 바꿈
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp

    return numbers

num = [4,7,3,5,8,9,1]
print(bubblesort(num))