import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

secret = random.randint(1, level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue

    if guess < secret:
        print("too small!")
    elif guess > secret:
        print("too large!")
    else:
        print("just right!")
        break
    