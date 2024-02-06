import sys
sys.stdin = open('input.txt')

T = int(input())

def f():
    pattern = input()
    text = input()

    pattern_len = len(pattern)
    text_len = len(text)

    text_idx = 0
    pattern_idx = 0

    while text_idx < text_len:
        if pattern[pattern_idx] != text[text_idx]:
            pattern_idx = -1

        pattern_idx += 1
        text_idx += 1

        if pattern_idx == pattern_len:
            return text_idx - pattern_len
    return None


for testcase in range(1, T+1):
    print(f())