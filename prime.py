n=int(input("enter no."))
l=[True]*(n+1)
l[0]=l[1]=False
for i in range(2,n+1):
    if (l[i]==True):
    
        for j in range(i*2,n+1,i):
            l[j]=False
            
for i in range(len(l)):
    if l[i]==True:
        print(i,end=',')