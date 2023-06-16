a = []
l = 0
b = 300
for i in range(12):
    n = int(input())
    a.append(n)
for i in range(12):
    b = b - a[i]
    if b<0:
        print(f'-{i+1}')
        break
    elif b>100:
        k = 0
        k = b //100
        b = b - 100 * k
        l = l + k
    b += 300
else:
    b = (b-300) + l*120
    print(b)
