n = int(input())
s = list(map(int,input().split()))
a = list(set(s))
b = sorted(a)
c = len(b)
print(c)
for i in range(c):
    print(b[i],end=' ')