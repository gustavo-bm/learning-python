#args are a tuple (ordered and unchangeable lists of values)

def add(*args): #args can be named as anything
    sum = 0
    #if you want to change a value, first convert to a list
    args = list(args)
    args[0] = 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5))