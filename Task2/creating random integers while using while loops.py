import random
for num in range(5, 10):
    print(num)

# or

# for a dice

sides = 6
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
count = 1

while sides == 4 and die1 != die2:
    print (count, ". die number 1 is", die1, "and die number 2 is", die2,".")
    count == count + 1
