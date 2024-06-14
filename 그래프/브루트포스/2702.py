import math

n = int(input())
input_list = []

# 입력 받기
for _ in range(n):
    row = list(map(int, input().split()))
    input_list.append(row)

# 최대공약수 함수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 각 쌍에 대해 최대공약수와 최소공배수 출력
for pair in input_list:
    a, b = pair
    gcd_value = gcd(a, b)
    lcm_value = (a * b) // gcd_value
    print(lcm_value, gcd_value)
    
