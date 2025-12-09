import random

def roll_function(amount):
    rolls = []
    for _ in range(amount):
        rolls.append(random.randint(1, 6))
    return rolls

rolls = roll_function(5)
pairs = [x for x in set(rolls) if rolls.count(x) == 2]

print("You rolled:", *rolls)

if any(rolls.count(x) == len(rolls) for x in set(rolls)):
    print("YAHTZEE! 🎉")
elif any(rolls.count(x) == 4 for x in set(rolls)):
    print("You got four of a kind!")
elif any(rolls.count(x) == 3 for x in set(rolls)):
    print("You got three of a kind!")
elif len(pairs) == 2:
    print("You got two pairs!")
elif pairs:
    print("You got a pair!")