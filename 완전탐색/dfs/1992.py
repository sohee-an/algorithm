n= int(input())

canvas=[list(map(int,input().strip())) for _ in range(n)]


def quard(y, x, size):
    if size == 1:
        return str(canvas[y][x])
    
    b = canvas[y][x]
    ret = ""
    for i in range(y, y + size):
        for j in range(x, x + size):
            if b != canvas[i][j]:
                ret += '('
                ret += quard(y, x, size // 2)
                ret += quard(y, x + size // 2, size // 2)
                ret += quard(y + size // 2, x, size // 2)
                ret += quard(y + size // 2, x + size // 2, size // 2)
                ret += ')'
                return ret
    
    return str(canvas[y][x])
print(quard(0, 0, n))