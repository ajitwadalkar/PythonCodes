#Given five positive integers, find the minimum and maximum values that can be calculated by summing
# exactly four of the five integers. Then print the respective minimum and maximum values as a
# single line of two space-separated long integers.

arr = [3,1,2,3,4,5]
sumOfArr = sum(arr)
maxVal = 0
minVal = sumOfArr
for i in arr:
    if maxVal < (sumOfArr - i):
        maxVal = sumOfArr - i
    if minVal > (sumOfArr - i):
        minVal = sumOfArr - i

print(maxVal)
print(minVal)
