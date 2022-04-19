import random

dice = [1, 2, 3, 4, 5, 6]

number = random.randint(0, 100) #random int from 0 to 100
print("Number: ", number)

number = random.choice(dice)
print("Dice: ", number)

