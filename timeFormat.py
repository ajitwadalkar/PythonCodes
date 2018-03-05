#Given a time in -hour AM/PM format, convert it to military (-hour) time.

s = "12:05:39AM"

h = int(s[0:2]) % 12
if s[-2] == "P":
    h = h+12
result = "%02d" % h + s[2:8]
print(result)