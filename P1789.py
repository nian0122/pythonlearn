n, m, k = map(int, input().split())
s = []
ans = 0
for i in range(n):
    c = []
    for j in range(n):
        c.append(0)
    s.append(c)
def pd(x,y):
    if(x < 1 or y < 1 or x > n or y > n):return 0
    return 1
for i in range(1,m + k + 1):
    a, b = map(int, input().split())
    for x in range(-2, 3):
        for y in range(-2, 3):
            if (i > m or abs(x) + abs(y) <= 2) and pd(x + a, y + b):
                s[x + a - 1][y + b - 1] += 1
for i in range(n):
    for j in range(n):
        ans += s[i][j] == 0
print(ans)