import random

def roll_function():
    return random.randint(1,6)

rolls = [roll_function() for _ in range(3)]

print("You rolled:", *rolls)

if rolls.count(6) == 3:
    print("All three rolls are sixes! 🎉")
elif len(set(rolls)) < len(rolls):
    print("At least one number is repeated!")
else:
    print("All rolls are different!")