import random

num = random.randint(1,50)
count = 1

while True:
    num2 = int(input("gebe eine Zahl zwischen 1 und 50 ein: "))
    count = count + 1

    if num2 < num:
        print('Die Zahl war zu niedrig')
    elif num2 > num:
        print('Die Zahl war zu hoch')
    else:
        print('Du hast die richtige Zahl erraten! Glückwusch!')
        print(f'Du hast {count} Versuche benötigt')
        break