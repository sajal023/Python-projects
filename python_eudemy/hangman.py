blank_lst = []
for i in choosen_word:
    blank_lst.append("_")
print(blank_lst)
end_of_game = 0

lives = 5

while not end_of_game:
    guess_word = input("Guess a word: ")
    if guess_word in blank_lst:
        print(f"you have guessed {guess_word} earlier")
    for i in range(l):
        if guess_word == choosen_word[i]:
            blank_lst[i] = guess_word
    if guess_word not in choosen_word:
        print(f"you have guessed wrong, {guess_word} not present in choosen letter")
        lives -= 1
        if lives==0:
            end_of_game=1
            print("OOPS!! bad luck!! NHK")
        print(stages[lives])
    print(blank_lst)
    if "_" in blank_lst:
        print("OOPS!! bad luck!! NHK")
    else:
        print("CONGRATULATIONS!!!! You Won")






