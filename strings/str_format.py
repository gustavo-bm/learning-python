#optional method to give more control when 
#displaying output

animal = 'dog'
item = 'fence'

print('The {} jumped over the {}'.format(animal, item))

print('The {0} jumped over the {1}'.format(animal, item))
print('The {1} jumped over the {0}'.format(item, animal))
#the placeholder {} (also called format field)  may have a index wich refers to the position of the value

print('The {animal} jumped over the {item}'.format(animal='cow', item='moon'))

text = 'The {} jumped over the {}'
print(text.format(animal, item))

text = 'Hi, my name is {} and I am {} years old. I like {} and my girlfriend is {}'
print()
name = str(input('Name: '))
age = int(input('Age: '))
like = str(input('Like: '))
girlfriend = str(input("Girlfriend's name: "))
print(text.format(name, age, like, girlfriend))

print()
print('Hello, my name is {}, nice to meet you'.format(name))
print('Hello, my name is {name:10}, nice to meet you'.format(name='gu'))
print('Hello, my name is {:>10}, nice to meet you'.format(name))
print('Hello, my name is {:<10}, nice to meet you'.format(name))
print('Hello, my name is {:^10}, nice to meet you'.format(name))

#numbers

number = 10245
print('The number is {:.3f}'.format(number))
print('The number is {:,}'.format(number)) #with the comas
print('The number is {:b}'.format(number)) #binary
print('The number is {:o}'.format(number)) #octal
print('The number is {:X}'.format(number)) #hex
print('The number is {:E}'.format(number)) #scientific notation
