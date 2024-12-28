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
