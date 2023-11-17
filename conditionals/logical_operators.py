temp = int(input('What is the temperature?'))

if temp >= 20 and temp <= 30:
    print('The temperature is good, go outside!')
elif temp < 20 or temp > 30:
    print('The temperature is bad, consider not going outside!')

if not(temp <= 0):
    print('The temperature is above 0.')