l=list(map(int,input().split()))
ans=0
for i in l:
    ans=ans^i
print(ans)