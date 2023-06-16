apple = list(map(int, input().split()))
high = int(input())
n=0
for i in apple:
    if i <= (high+30):
        n += 1
print(n)