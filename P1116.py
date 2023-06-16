n = int(input())
s=[]
while len(s)<n:
    s+=[int(i) for i in input().split()]
m = 0
for i in range(n):
    for j in range(i):
        if s[j]>s[i]:
            m+=1
print(m)
