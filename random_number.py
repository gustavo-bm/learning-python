import random

#pseudo random generation

dice = random.randint(1, 6)
print(dice)

y = random.random() #generate a number between 0 and 1
print(y)

rps = ['Rock', 'Paper', 'Scisors']
choice = random.choice(rps)
print(choice)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)


