import re
for test_string in ['555-1212', '513-641-8182']:
    if re.match(r'^\d{3}-\d{3}-\d{4}$', test_string):
        print (test_string, 'is a valid US local phone number')
    else:
        print (test_string, 'rejected')

m = re.search('(?<=abc)def', 'abcdef')
m.group(0)
print(m)

m = re.search('(?<=-)\w+', 'spam-egg')
m.group(0)
print(m)