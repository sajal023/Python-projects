import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u, c):
    if u == c:
        return ("!Draw ':(' ")
    elif c == 0 or u > 21:
        return ("!!OOPS !you loose!'＞﹏＜'")
    elif u == 0 or c > 21:
        return ("!!Congrats you win!'（￣︶￣）'")
    else:
        if u > c:
            return ("!!Congrats you win!'（￣︶￣）'")
        else:
            return ("!!OOPS !you loose!'＞﹏＜'")


def restart():
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    end_of_game = False

    while end_of_game == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards: {user_cards}, your score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_of_game = True
        else:
            choice = input("enter 'yes' to draw another card and 'no' to pass: ")
            if choice == "yes":
                user_cards.append(deal_card())
            else:
                end_of_game = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


ask_user = input("want to play the game: type 'y' or 'n'")
if ask_user == "y":
    restart()
else:
    print("you should have gave it a try!! no offence😄")
