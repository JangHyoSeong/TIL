def f(i, k, s, t): # 합이 t인 부분집합 구하기
    if s == t:      # 구하는 합을 얻었다면
        
        for j in range(k):  # 모든 bit를 순회함
            if bit[j]:
                print(A[j], end = ' ')
        print()

    elif i==k:    # 모든 원소를 고려했으나 s!=t인 경우
        return
    elif s > t:     # 고려한 원소의 합이 t보다 큰 경우
        return

    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)
        bit[i] = 0
        f(i+1, k, s, t)



N = 10
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

bit = [0] * N

f(0, N, 0, 10)