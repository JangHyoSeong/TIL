print(int(10)) # 10진수
print(bin(10)) # 2진수, 문자열
print(oct(10)) # 8진수, 문자열
print(hex(10)) # 16진수, 문자열

# base -> 진수표현을 의미, 16진법으로 표현된 10을 10진수로 바꿈 -> 16
print(int('F', base=16))

print(bin(8)) # 1000
print(bin(1)) # 1
# 비트수를 맞춰줘야 할 필요가 있음. zfill method 사용

# 2번째 인덱스부터 '0'으로 4글자가 될때까지 채워라
print(bin(1)[2:].zfill(4))
for i in range(16):
    print(hex(i)[2:])

# 16진법 -> 2진법
print(bin(int('A', base=16))[2:].zfill(4))

# fstring 사용 가능
bin_to_hex = {}
for i in range(16):
    print(f'{i:04b}')
    bin_to_hex[f'{i:04b}'] = hex(i)[2:].upper()
print(bin_to_hex)

hex_to_bin = {hex(i).replace('0x', '').upper(): f'{i:04b}' for i in range(16)}
print(hex_to_bin)