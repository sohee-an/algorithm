import math

def is_square(num):
   
    if num < 0:
        return False
    root = int(math.isqrt(num))
    return root * root == num

def search(x, y, step_x, step_y):
   
    num_str = ""
    while 0 <= x < n and 0 <= y < m:
        num_str += graph[x][y]
        num = int(num_str)
        if is_square(num):
            global largest_square
            largest_square = max(largest_square, num)
        x += step_x
        y += step_y

n, m = map(int, input().split())
graph = [input().strip() for _ in range(n)]

largest_square = -1

for i in range(n):
    for j in range(m):
        for step_x in range(-n, n):
            for step_y in range(-m, m):
                if step_x == 0 and step_y == 0:
                    continue
                search(i, j, step_x, step_y)

print(largest_square)
