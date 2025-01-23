from itertools import combinations

def find_seven_dwarfs(heights):
    print("h",heights)
    # heights 리스트에서 7개를 선택하는 모든 조합을 탐색
    for combo in combinations(heights, 7):
        # 조합의 합이 100이면 반환
        if sum(combo) == 100:
            return combo

# 9명의 난쟁이들의 키 입력
heights = []
for _ in range(9):
    heights.append(int(input()))

# 7명의 난쟁이들의 키를 찾음
result = find_seven_dwarfs(heights)

# 결과 출력
for height in result:
    print(height)
