mat=[ [1, 2, 3],[4, 9, 6],[7, 8, 9] ]
k=2

for i in range(len(mat)-1):
    for j in range(len(mat[0])-1):
        if mat[i][j]==k:
            res=(i+1)*1009+(j+1)
            poi=i+1
            poj=j+1
            break
            
        else:
            pass
print(f"k is found at i={poi} and j={poj} so value is {res}")
