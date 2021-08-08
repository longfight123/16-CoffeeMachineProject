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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "profit": 0
}


def check_resources_sufficient(drink_type):

    if drink_type == 'espresso':
        if MENU[drink_type]["ingredients"]["water"] > RESOURCES["water"]:
            print('Sorry there is not enough water.')
            return False
        if MENU[drink_type]["ingredients"]["coffee"] > RESOURCES["coffee"]:
            print('Sorry there is not enough coffee.')
            return False
    if drink_type in ['cappuccino', 'latte']:
        if MENU[drink_type]["ingredients"]["water"] > RESOURCES["water"]:
            print('Sorry there is not enough water.')
            return False
        if MENU[drink_type]["ingredients"]["coffee"] > RESOURCES["coffee"]:
            print('Sorry there is not enough coffee.')
            return False
        if MENU[drink_type]["ingredients"]["milk"] > RESOURCES['milk']:
            print('Sorry there is not enough milk.')
            return False
    return True


def check_coins_sufficient(quarters_inserted, dimes_inserted, nickels_inserted, pennies_inserted, drink_type):

    total_coins_inserted = quarters_inserted + dimes_inserted + nickels_inserted + pennies_inserted
    if total_coins_inserted >= MENU[drink_type]['cost']:
        change = round(total_coins_inserted - MENU[drink_type]['cost'], 2)
        print(f'Here is your change: {change}$')
        return True
    else:
        print('Sorry that is not enough money. Money refunded.')
        return False


def make_a_drink():

    user_drink = input('Hello, what would you like? (espresso/latte/cappuccino)')
    if user_drink == 'report':
        print(f'Water: {RESOURCES["water"]}ml\nMilk: {RESOURCES["milk"]}ml\nCoffee {RESOURCES["coffee"]}ml\n'
              f'Money {RESOURCES["profit"]}$')
    elif user_drink == 'off':
        return
    elif user_drink in ['espresso', 'latte', 'cappuccino']:
        if not check_resources_sufficient(user_drink):
            make_a_drink()
        print('Please insert coins:')
        quarters = int(input('Quarters:'))*0.25
        dimes = int(input('Dimes:'))*0.1
        nickels = int(input('Nickels:'))*0.05
        pennies = int(input('Pennies:'))*0.01
        if not check_coins_sufficient(quarters_inserted=quarters, dimes_inserted=dimes,
                                      nickels_inserted=nickels, pennies_inserted=pennies, drink_type=user_drink):
            make_a_drink()
        if user_drink == 'espresso':
            RESOURCES['water'] -= MENU[user_drink]['ingredients']['water']
            RESOURCES['coffee'] -= MENU[user_drink]['ingredients']['coffee']
        elif user_drink in ['latte', 'cappuccino']:
            RESOURCES['water'] -= MENU[user_drink]['ingredients']['water']
            RESOURCES['coffee'] -= MENU[user_drink]['ingredients']['coffee']
            RESOURCES['milk'] -= MENU[user_drink]['ingredients']['milk']
        RESOURCES['profit'] += MENU[user_drink]['cost']
        print(f'Here is your drink: {user_drink}')
    else:
        print('That is not a valid drink.')
    make_a_drink()


make_a_drink()
