#set is a collection, a list with unordered and unindexed values

colors = {'red', 'green', 'blue', 'yellow', 'yellow', 'orange'}
#no duplicated values
items = {'shirts', 'hat', 'gloves', 'socks'}

for x in colors:
    print(x + ' ', end='')

print()
colors.remove('red')
colors.add('brown')

for x in colors:
    print(x)
print()

colors.update(items) #the second set goes inside the first
for x in colors:
    print(x)
print()

collection = colors.union(items)
for x in collection:
    print(x)
print()

items.add('orange')
print(colors.difference(items)) #values in colors but not in items
#intersection works similarly