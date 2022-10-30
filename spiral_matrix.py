n = int(input())

a = [[0]*n for _ in range(n)]

i = 1
x = 0
dx = 0
y = -1
dy = 1

while i <= n**2:
    if x+dx < n and y+dy < n and a[x+dx][y+dy] == 0:
        x += dx
        y += dy
        a[x][y] = i
        i += 1
    else:
        if dy == 1:
            dy = 0
            dx = 1
        elif dx == 1:
            dx = 0
            dy = -1
        elif dy == -1:
            dy = 0
            dx = -1
        elif dx == -1:
            dx = 0
            dy = 1
