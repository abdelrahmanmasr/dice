import random

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
count = 1

while die1 != die2:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print(count, ". die number 1 is", die1, "and die number 2 is", die2,".")
    count = count + 1
