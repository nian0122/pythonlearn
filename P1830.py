r = []
f = []
x0 = []
y0 = []
n, m, x, y = map(int, input().split())
for i in range(n):
    c = []
    d = []
    for j in range(m):
        c.append(0)
        d.append(0)
    r.append(c)
    f.append(d)
for i in range(x):
    d = list(map(int, input().split()))
    x0.append(d)
for i in range(y):
    d = list(map(int, input().split()))
    y0.append(d)
for _ in range(x):
    for a in range(x0[_][0]-1,x0[_][2]):
        for b in range(x0[_][1]-1,x0[_][3]):
            r[a][b] += 1
            p = _ + 1
            f[a][b] = p
for i in range(y):
    if r[y0[i][0]-1][y0[i][1]-1] != 0:
        print(f"Y {r[y0[i][0]-1][y0[i][1]-1]} {f[y0[i][0]-1][y0[i][1]-1]}")
    else:
        print("N")