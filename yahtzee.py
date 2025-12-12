import random

small_straights = [{1,2,3,4}, {2,3,4,5}, {3,4,5,6}]
large_straight = [{1,2,3,4,5}]

def roll_dice (amount):
    dice = []
    for _ in range(amount):
        dice.append(random.randint(1, 6))
    return dice

rolled_dice = roll_dice(5)
doubles = [x for x in set(rolled_dice) if rolled_dice.count(x) == 2]
tripples = [x for x in set(rolled_dice) if rolled_dice.count(x) == 3]
quads = [x for x in set(rolled_dice) if rolled_dice.count(x) == 4]

print("You rolled:", *rolled_dice)

if any(rolled_dice.count(x) == len(rolled_dice) for x in set(rolled_dice)):
    print(f"YAHTZEE! 🎉")
elif quads:
    print(f"You got four of a kind! {quads[0]}'s")
elif any(straight == set(rolled_dice) for straight in large_straight):
    print(f"You got a large straight! " + " ".join(str(x) for x in large_straight[0]))
elif any(straight.issubset(rolled_dice) for straight in small_straights):
    print(f"You got a small straight! " + " ".join(str(x) for x in small_straights[0]))
elif doubles and tripples:
    print(f"You got a full house! {tripples[0]}'s full of {doubles[0]}'s")
elif tripples:
    print(f"You got three of a kind! {tripples[0]}'s")
elif len(doubles) == 2:
    print(f"You got two pairs! " + " and ".join(f"{x}'s" for x in doubles))
elif doubles:
    print(f"You got a pair of {doubles[0]}'s!")