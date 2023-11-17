name = 'Gustavo Bianchini Moraes'

first_name = name[0:7] #or name[:7], whatever
#the first index is inclusive
#the last index is exclusive

print(first_name)

last_name = name[8:]
print(last_name)

funky_name = name[0:24:1]
print(funky_name)

reversed_name = name[::-1]
print(reversed_name)

website = 'https://www.youtube.com/'
print(website.find('y'))
slice_ = slice(12,-5)
print(website[slice_])