a=[[1,0,1],[1,1,1],[1,1,1]]
m=len(a)
n=len(a[0])
b=[1]*m
c=[1]*n

for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            b[i]=0
            c[j]=0
            
            
for i in range(3):
    for j in range(3):
        if b[i]==0 or c[j]==0:
            a[i][j]=0
for i in a:
    print(i)