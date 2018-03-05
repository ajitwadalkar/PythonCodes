#absolute sum of diagonal elements
a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
n = len(a)
diagonalOne = sum(a[i][i] for i in range(n))
diagonalTwo = sum(a[i][n-i-1] for i in range(n))
print(diagonalOne)
print(diagonalTwo)
finalSum = abs(diagonalOne+diagonalTwo)
print(finalSum)
