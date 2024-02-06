import sys
sys.stdin = open('input.txt')

def palindrome(arr, m):
    for word in arr:
        for s in range(100 - m + 1):
            for k in range(m//2):
                if word[s+k] != word[s + m -1 -k]:
                    break
            else:
                return m
    return 0
 
for t in range(1, 11):
    N = int(input())
    lst1 = list(input() for _ in range(100))
    lst2 = list(''.join(x) for x in zip(*lst1))
 
    ans = 1
    for m in range(2, 101):
        if m > ans + 2: break
        if ans < palindrome(lst1, m):
            ans = m
 
    m = ans + 1
    for m in range(ans + 1, 101):
        if m > ans + 2: break
        if ans < palindrome(lst2, m):
            ans = m
 
    print('#%d %s' % (t, ans))