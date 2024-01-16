import math

# 원주율
3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
15


pi = math.pi
radius = 15
pi_is = '원주율 : '
radius_is = '반지름 : '
perimeter_is = '원의 둘레 : '
area_is = '원의 넓이 : '
print(pi_is, pi)
print(radius_is, radius)
print(perimeter_is, radius * 2 * math.pi)
print(area_is, radius ** 2 * math.pi)