from collections import deque
q=deque()
Max=100000
visited = [False] * (Max + 1)
# def bfs(n, k):
#     MAX = 100000
#     visited = [False] * (MAX + 1)
#     q = deque()
#     q.append((n, 0))   # (현재 위치, 이동 횟수)
#     visited[n] = True

#     while q:
#         cx, c_count = q.popleft()

#         # 목표 도착
#         if cx == k:
#             return c_count

#         for nx in (cx-1, cx+1, cx*2):
#             if 0 <= nx <= MAX and not visited[nx]:
#                 visited[nx] = True
#                 q.append((nx, c_count+1))
# n이 수빈이 k가 동생

def bfs(n,k):
    q.append([n,0])
    visited[n]=True
    
    while q:
        cx,count=q.popleft()
        if cx==k:
            return count
        for nx in (cx+1,cx-1,cx*2):
            if 0<=nx<=Max and visited[nx]==False:
                visited[nx]=True
                q.append([nx,count+1])
    

n, k = map(int, input().split())
print(bfs(n, k))
