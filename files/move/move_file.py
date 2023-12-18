import os

src = "test.txt"
dest = "D:\\UFScar"

try:
    if os.path.exists(dest):
        print("There is already a file there")
    else:
        os.replace(src, dest)
        print(src + " was moved sucessfully!")
except FileNotFoundError:
    print(src + " was not found")