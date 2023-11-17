#like a args but with a dictionary instead of a tuple

def hello(**kwargs):
    print('Hello, ' + kwargs['first'] + ' ' + kwargs['last'])

hello(first='Gustavo', middle='Bianchini',last='Moraes')

def hello_2(**kwargs):
    print('Hello, ', end='')
    for i in kwargs:
        print(kwargs[i] + ' ', end='')

hello_2(first='Gustavo', middle='Bianchini',last='Moraes')
