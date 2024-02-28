'''
친구 {A,B,C,D,E}중에 2명 이상의 친구를 선정하여 함께 카페에 가려고 한다
몇가지 경우의 수가 가능한가
'''
arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

def get_sub(tar):
    count = 0
    for i in range(n):
        if tar & 0x1:
            count += 1
        tar >>= 1
    return count

result = 0
for tar in range(1<<n):

    count = get_sub(tar)

    if count >= 2:
        result += 1

print(result)

############################################
def get_count(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1

    return cnt

result = 0
for tar in range(1 << n):
    if get_count(tar) >= 2: # 비트가 2개 이상 1이라면 (2명 이상이라면)
        result += 1
print(result)