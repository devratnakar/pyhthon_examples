a=int(input())
num=0
i=0
while a:
    num=num+((a%2)*1<<(31-i))
    a=a//2
    i+=1
print(num)