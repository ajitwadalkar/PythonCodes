n=6
A=[5, 2, 3, 6, 6, 5]
A.sort(reverse=True)
for i in range (n):
    if A[i]!=A[0]:
        print(A[i])
        break
