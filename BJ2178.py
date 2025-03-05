import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]  # 입력 수정

q = deque([(0, 0)])

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

while q:
    y, x = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                q.append((ny, nx))

print(maps[n - 1][m - 1])  # 마지막 값 출력
