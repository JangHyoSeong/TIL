def KMP(pattern, target):

    def make_lps():
        # 내 앞에 나와 동일한 패턴이 몇번 나왔는지 세는 리스트
        lps = [0] * len(pattern)
        for idx in range(1, len(pattern)):  # 0번 인덱스는 앞에 중복되는 값이 없음
            if pattern[lps[idx-1]] == pattern[idx]:
                lps[idx] = lps[idx - 1] + 1
        lps[0] = -1
        return lps
    

    lps = make_lps()