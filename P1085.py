max = 0
day = 0
for _ in range(7):
    a, b = map(int,input().split())
    c = a + b
    if max<c and c>8:
        max = c
        day = _ + 1
print(day)
