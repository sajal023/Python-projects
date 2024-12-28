import random


def easy():
    lives = 10
    end = False
    print("you've got 10 attempts to guess the number.")
    working(lives)


def hard():
    lives = 5
    print("you've got 5 attempts to guess the number.")
    working(lives)


def working(lives):
    end = False
    while end == False:
        guess = int(input("make a guess: "))
        if guess < n:
            print("too low")
            print(f"you've got {lives - 1} attempt")
            print("guess again")
        elif guess > n:
            print("too high")
            print(f"you've got {lives - 1} attempt")
            print("guess again")
        lives = lives - 1
        if lives > 0:
            if guess == n:
                print(f"you've got the number i.e. {guess}")
                end = True
        else:
            print("out of attempt")
            end = True


print("welcome to the guess the number game!!")
n = random.randint(1, 100)

level_choose = input("choose a level: 'easy' or 'hard': ")
if level_choose == "easy":
    easy()
else:
    hard()
