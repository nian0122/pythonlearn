tree,n=map(int,input().split())
s = []
k = 0
for _ in range(tree+1):
    s.append(0)
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x,y+1):
        if s[i]==0:
            s[i] =1
for _ in s:
    if _==0:
        k+=1
print(k)