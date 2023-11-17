age = int(input('How old are you? '))

if age >= 18:
    print('You can get arrested!!!')
elif age < 3:
    print('Omg how are you even understanding that!?')
elif age == 150 or age >= 150:
    print('Bullshit.')
else:
    print('Go eat some ground')


if age == 150 or age >= 150:
    print('Bullshit.')
elif age < 3:
    print('Omg how are you even understanding that!?')
elif age >= 18:
    print('You can get arrested!!!')
else:
    print('Go eat some ground')   

    #the order matters, if the condition of the first if is true, the elsifs are skipped