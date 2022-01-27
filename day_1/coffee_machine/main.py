MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def user_prompt():
    """Prompts user from input and triggers coffee machine logic based on selection"""
    user_input = input('What would you like? (espresso/latte/cappuccino): ')
    if user_input == 'off':
        off()
    elif user_input == 'report':
        print_report()
    elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
        drink = MENU[user_input]
        make_coffee(user_input, drink["ingredients"])
    else:
        print('Not a valid option')


def off():
    """Turns the machine off"""
    print('Bye!')
    exit()


def print_report():
    """Prints report of resources"""
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: ${profit}')


def check_resources(ingredients):
    """Returns True if an order can be processed, False if insufficient ingredients"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print('Sorry there is not enough water')
            return False
    return True


def process_coins():
    """Prompts user to introduce coins and returns the amount of money introduced"""
    print('Please insert coins')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))

    return quarters * 0.25 + dimes * 0.1 + nickles * 0.5 + pennies * 0.1


def check_transaction(payment, cost):
    """Checks whether the user introduced enough money for their beverage selection"""
    if payment > cost:
        change = round(payment - cost, 2)
        print(f'Here is ${"{:.2f}".format(change)} in change')
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink, ingredients):
    """If we have enough resources and the payment amount is correct, we make the coffee and reduce
     the amount of resources left"""
    if check_resources(ingredients):
        money_introduced = process_coins()
        if check_transaction(money_introduced, MENU[drink]["cost"]):
            for item in ingredients:
                resources[item] -= ingredients[item]
            print('Here is your ' + drink + '. Enjoy!')


while True:
    user_prompt()




