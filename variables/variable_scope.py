#scope = region where the variable is recognized
name = 'gu global'


def print_name():
    name = 'gu local'
    print(name)


print_name() #prints the local variable
print(name) #prints the global variable