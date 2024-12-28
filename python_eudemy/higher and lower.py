from hangman_art import logo_2, vs
from game_data import data
import random


def to_display(acc):
    acc_name = acc['name']
    acc_desc = acc['description']
    acc_country = acc['country']
    return f" {acc_name}, {acc_desc}, {acc_country} "


def check(guess, account_a, account_b):
    if account_a > account_b:A
        return guess == 'A'
    else:
        return guess == 'B'


print(logo_2)

score = 0
end = 0
while end == 0:
    acc_a = random.choice(data)
    acc_b = random.choice(data)
    if acc_a == acc_b:
        acc_b = random.choice(data)
    A = acc_a["follower_count"]
    B = acc_b["follower_count"]

    print(f"compare A: {to_display(acc_a)}")
    print(vs)
    print(f"Against B: {to_display(acc_b)}")
    ty = input("Who has more followers? Type 'A' or 'B': ")
    x = check(ty, A, B)
    if x:
        score += 1
        print(f"you guessed it right! final score={score}")
    else:
        print(f"Guessed wrong!!, final score={score}")
        end = 1
