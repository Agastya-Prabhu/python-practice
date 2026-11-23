import random

roll = 0

while roll != 6:
    roll = random.randint(1, 6)
    if roll != 6:
        print(roll)

print("You rolled a 6!")