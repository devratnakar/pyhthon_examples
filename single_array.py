arr=list(map(int,input().split()))
s=0
for i in arr:
    s=s^i
print(s)