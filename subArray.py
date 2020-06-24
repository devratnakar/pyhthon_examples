A = [1, 2, 10,5, -7, 2, 3,7]
def sArray(A):
    n = 0;
    i = 0;
    
    ans=0
    index = []
    while i< len(A):
        start = i
        end = start
        summ = 0

        while i < len(A) and A[i]>=0:
            summ += A[i]
            end += 1
            i += 1
        if summ > ans:
            ans = summ
            index.append([start, end])
            n +=1
        i +=1
    return A[index[n-1][0]:index[n-1][1]]
print(sArray(A))