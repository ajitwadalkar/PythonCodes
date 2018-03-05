arr = [-4, 3, -9, 0, 4, 1 ]

neg = 0.0
pos = 0.0
zer = 0.0
for i in arr:
    if i < 0:
        neg += 1;
    if i > 0:
        pos += 1;
    if i==0:
        zer += 1;
sum = neg + pos + zer
neg = neg / sum
pos = pos / sum
zer = zer / sum
print("%.6f" % pos)
print("%.6f" % neg)
print("%.6f" % zer)