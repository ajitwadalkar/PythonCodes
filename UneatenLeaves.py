import math
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   comp = 0
   while(True):
       comp += 1
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm, comp


a = [2, 3, 5, 4, 9, 24]
n = 50
comp =0
coveredleaves = []
leavedict = {}
for i in a:
    count = math.floor(n / i)
    for j in coveredleaves:
        comp += 1
        if leavedict[j] == 0:
            continue
        num, comp2 = lcm(i, j)
        if num == i:
            count = 0
            break
        elif num == j:
            count -= leavedict[j]
        else:
            count -= math.floor(n / num)
    coveredleaves.append(i)
    leavedict[i] = count

print(n - sum(leavedict.values()))
print(comp)
print(comp2)