# You are given a sequence of integers a1,a2,a3.....an. You are free to replace any integer with any other positive integer.
# How many integers must be replaced to make the resulting sequence strictly increasing?

# arr = [1, 7, 10, 2, 20, 22]
#arr = [4,10, 20]
#arr = [1, 2, 2, 3, 4 ]
#arr = [602339555, 833991, 551120223, 2, 893538124, 415344255, 2645, 372902617, 155, 63758095, 3080]
arr = [8, 3, 8, 9, 8, 1, 6, 2, 10]
count = 0
for i in range(len(arr)):
    if i == len(arr)-1:
        break
    if arr[i] >= arr[i+1]:

        arr[i+1] = arr[i]+1
        count += 1

print(arr)
print(count)
