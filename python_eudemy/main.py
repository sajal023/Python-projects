'''from cipher_art import logo
import string

print(logo)


def caesar(command, t, s):
    cipher_text = ""
    if command == 'D':
        s = s * -1
    for i in t:
        if i in alphabet:
            pos_letter = alphabet.index(i)
            new_pos = pos_letter + s
            cipher_text += alphabet[new_pos]
        else:
            cipher_text += i
    print(f"the coded text is {cipher_text}")


alphabet = list(string.ascii_letters + string.ascii_letters)
end = 0
while not end:
    command = input("Enter 'E' for encoding or 'D' for decoding: ")
    text = input("enter the text for operation")
    shift_no = int(input("Enter the shift number: "))
    shift_no %= 26
    caesar(command, text, shift_no)
    choice = input("Enter 'again' to begin operation or 'end' to exit: ")
    if choice == 'end':
        end = 1
'''

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

end = 0
while end == 0:
    options = menu.get_items()
    choice = input(f"what would you like to have? {options} ")
    if choice == "off":
        end = 1
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        x = coffee_maker.is_resource_sufficient(drink)
        if x:
            if money_machine.make_payment(drink.cost):
                print(coffee_maker.make_coffee(drink))
            else:
                end = 1
        else:
            end = 1
