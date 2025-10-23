import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))

# # 이건 시간초과남 
# for _ in range(m):
#     i, j = map(int, input().split())
#     total = 0
#     for k in range(i, j + 1):
#         total += arr[k - 1]
#     print(total, end="\n")
    
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i - 1]

results = []  # ✅ 결과 저장 리스트
for _ in range(m):
    i, j = map(int, input().split())
    results.append(str(prefix[j] - prefix[i - 1]))  # 문자열로 저장

print("\n".join(results))  # ✅ 한 번에 줄바꿈으로 출력


    
    