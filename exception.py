#exception is an event wich causes an interruption on the program,
#interrupting its flow
while (1): #to make it repeat indefinitely
    try:
        numerator = int(input('Enter a numerator: '))
        denominator = int(input('Enter a denominator: '))
        result = numerator / denominator
    except ZeroDivisionError as e:
        print(e)
        print('You cannot divide by zero, dumbass!!!')
    except ValueError as e:
        print(e)
        print('A number... dont you know what a number is?')
    except Exception as e:
        print(e)
        print('Something got an error')
    else:
        print(result)
    finally:
        print('This will always execute')