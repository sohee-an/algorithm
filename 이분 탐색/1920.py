n = int(input())
n_arr = list(map(int, input().split()))
m = int(input())
m_arr = list(map(int, input().split()))

n_arr.sort()

def binary_search(array, target):
    start = 0
    end = len(array)  # [start, end)

    while start < end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid

    return 0

result = []
for v in m_arr:  # 입력 순서 유지
    result.append(binary_search(n_arr, v))

print(*result, sep="\n")
