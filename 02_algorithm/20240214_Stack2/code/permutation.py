
def f(i, N):
    if i == N:
        print(*P)
    else:
        for j in range(i, N):     # P[i]자리에 올 원소 P[j]를 결정
            P[i], P[j] = P[j], P[i]
            f(i+1, N)               # 다음 자리를 결정하러 이동
            P[i], P[j] = P[j], P[i] # 원상 복구




P = [1, 2, 3]
N = 3

f(0, N)