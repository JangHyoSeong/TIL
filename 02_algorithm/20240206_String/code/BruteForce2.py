def BruteForce(pattern, text, M, N):
    for i in range(N-M+1):
        for j in range(M):
            if text[i+j] != pattern[j]:     # 불일치하면 다음 시작위치로 이동
                break
        else:       # 불일치 하지 않았으면 찾은것, return으로 위치를 반환
            return i
    
    return -1


def bruteForce_2(pattern, target):

    # 조사지점은 0번부터 시작
    pattern_index = 0
    target_index = 0

    # 현재 조사위치가 조사대상의 범위를 벗어나기 전까지
    while target_index < len(target):

        # 일치하지 않았다면 초기화
        if pattern[pattern_index] != target[target_index]:
            pattern_index = -1
        # 일치하면 인덱스 증가
        target_index += 1
        pattern_index += 1


        # 패턴의 끝까지 인덱스가 닿는다면 -> 모두 일치했다면
        # True 반환
        if pattern_index == len(pattern):
            return True
        
    # target을 전부 순회할때까지 True를 반환하지 못했다면 False반환    
    return False


T = int(input())
for testcase in range(1, T+1):
    pattern = input()
    text = input()
    M = len(pattern)
    N = len(text)

    print(BruteForce(pattern, text, M, N))