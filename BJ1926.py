import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

cnt = 0
mx = 0

def bfs(y, x):
    q = deque([(y, x)])
    s = 1
    visited[y][x] = True
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    while q:
        y, x= q.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1 and visited[ny][nx] == False:
                q.append((ny, nx))
                visited[ny][nx] = True
                s += 1
                
    return s
                
for j in range(n):
    for i in range(m):
        if maps[j][i] == 1 and visited[j][i] == False:
            mx = max(bfs(j, i), mx)
            cnt += 1
            
print(cnt)
print(mx)
