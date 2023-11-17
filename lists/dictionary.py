#key:value pairs, unordered and changeable collection

capitals = {'Brasil':'Rio de Janeiro',
           'USA':'Washington DC',
           'China':'Beijing'
           }

print(capitals.get('Brasil'))
print()

print(capitals.keys())
print()

print(capitals.values())
print()

print(capitals.items())
print()

for key,value in capitals.items():
    print(key, value)
print()

capitals.update({'Germany':'Berlin'})
capitals.update({'Brasil':'Brasília'})
capitals.pop('USA')

for key,value in capitals.items():
    print(key, value)
print()

capitals.clear()
