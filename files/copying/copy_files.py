# copyfile() = copies the contents of a file
# copy() = copyfile + permission mode + destination can be a directory
# copy2() =copy + copies metadata (file's creation and modification times)

import shutil

src = 'SHEEEESH'
dest = ''

with open('C:\\Users\\gusta\\python\\files\\copying\\src.txt', 'w') as file:
    file.write(src)

shutil.copyfile('C:\\Users\\gusta\\python\\files\\copying\\src.txt', 'C:\\Users\\gusta\\python\\files\\copying\\dest.txt') #src -> dest

with open('C:\\Users\\gusta\\python\\files\\copying\\dest.txt') as file:
    print(file.read())