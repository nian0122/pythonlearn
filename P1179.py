def pd1(i):
    n = 0
    while i != 0:
        i //= 10
        n +=1
    return n

def pd2(i):
    n = 0
    for _ in range(pd1(i)):
        j = i % 10
        i //= 10
        if j == 2:
            n += 1
    return n
l, r =map(int, input().split())
a = 0
for i in range(l,r+1):
    a += pd2(i)
print(a)
