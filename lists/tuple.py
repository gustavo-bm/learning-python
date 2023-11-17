#lists but ordered and unchangeable

student = ('gu', 18, 'male')

print(student.count('male')) #how many times it appears
print(student.index('male')) #position of the element

for x in student:
    print(x)

if 'gu' in student:
    print('gu is here')