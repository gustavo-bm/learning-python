import os

path = "C:\\ED-1\\AT-1\\atividade-1.c" #always use double back slashs

if os.path.exists(path):
    print('That location exists')
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")