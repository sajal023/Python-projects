from game_data import MENU

coffee_moneybox = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def res_suff(c_ingredients):
    for i in c_ingredients:
        if resources[i] > c_ingredients[i]:
            return True
        else:
            return False


def make_coffee(c_ingredients):
    for i in c_ingredients:
        resources[i] -= c_ingredients[i]
    print(f"here is your {choice} enjoy!")
    return resources


user = 1
while user:
    choice = input("what would you like? ('espresso'/'latte'/'cappuccino'/'report'/'off')")
    if choice == "off":
        user = 0
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffe: {resources['coffee']}g")
        print(f"money: {coffee_moneybox}$")
    else:
        drink = MENU[choice]
        print(drink)
        w = res_suff(drink["ingredients"])
        if w:
            print("insert the coins")
            q = int(input("how many quarters: ")) * 0.25
            d = int(input("how many dimes: ")) * 0.10
            n = int(input("how many nickles: ")) * 0.05
            p = int(input("how many pennies: ")) * 0.01
            sum_coins = q+d+p+n
            print(sum_coins)
            if sum_coins >= drink["cost"]:
                coffee_moneybox += drink["cost"]
                print(f"here is ${sum_coins - drink['cost']} in change")
                after_report = make_coffee(drink["ingredients"])
                if choice == "report":
                    print(after_report)
            else:
                print("not enough")
        else:
            print("Sorry there is not enough water")
            user = 0
