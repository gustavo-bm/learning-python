friends = ['Natalia', 'Leonardo', 'Thiago', 'Larissa']

print(friends[0])
friends.remove('Natalia')
# friends.pop() #remove the last
friends.insert(0, 'Saggion')
friends.sort() #organizes in alhabetic order

for i in friends:
    print(i)

friends.clear()
for i in friends:
    print(i)