students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students.sort(key=lambda l: l[1])
r = []
p = 0
for i in range(len(students)):
    if students[i][1] != students[0][1]:
        if p == 0:
            r.append([])
            r[p] = i
            p += 1
        else:
            if students[r[p - 1]][1] == students[i][1]:
                r.append([])
                r[p] = i
                p += 1
            else:
                break

newlist = []
for i in range(p):
    newlist.append([])
    newlist[i] = students[r[i]][0]

newlist.sort()

for i in range(p):
    print(newlist[i])
