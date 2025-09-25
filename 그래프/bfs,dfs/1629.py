# 자연수 A를 B번 곱한 수를 알고 싶다.
# 단 구하려는 수가 매우 커질 수 있으므로 
# 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
A, B, C = map(int, input().split())

def pow_mod(a, b, c):
    if b == 0:
        return 1 % c   # b가 0일 때 안전하게 처리
    half = pow_mod(a, b // 2, c)
    result = (half * half) % c
    if b % 2 == 1:   # 홀수면 a 한 번 더 곱하기
        result = (result * a) % c
    return result

print(pow_mod(A, B, C))
