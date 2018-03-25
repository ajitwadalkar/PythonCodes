x = 1
y = 1
z = 1
n = 2
ar = []
p = 0
for i in range (0,x+1):
    for j in range (0,y+1):
        for k in range (0,z+1):
            if i+j+k != n:
                ar.append([])
                ar[p] = [i,j,k]
                p+=1

print(ar)