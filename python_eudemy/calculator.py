def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    n1 = float(input("enter the first number: "))
    for i in operations:
        print(i)
    end = 0

    while end == 0:
        choice = input(f"enter the operation: ")
        n2 = float(input("enter the next number: "))
        function = operations[choice]
        x = function(n1, n2)
        print(f"{n1} {choice} {n2} = {x}")
        ahead = input(f"enter 'y' to continue with {x} or 'n' to start new calculation: ")
        if ahead == "y":
            n1 = x
        else:
            print("#######################################################################################################################################################################")
            end = 1
            calculator()  #concept of recursion


calculator()
