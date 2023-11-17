columns = int(input('How many columns? '))
rows = int(input('How many rows? '))
symbol = input('Enter a symbol: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end = '') #prevents from /n
    print() #it's the /n