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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_coffee(name):
    coffe_ingredients = MENU[name]['ingredients']
    for item in coffe_ingredients:
        resources[item] -= coffe_ingredients[item]
    print(f"Here is your {name}☕ enjoy!")


profit = 0


def calculate(cost, quarters, dimes, nickels, penis, coffe):
    global profit
    cost = cost
    amount = 0
    amount = 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * penis
    if amount == cost:
        profit += cost
        print("Thanks for Payment ✔")
        make_coffee(coffe)
    elif amount >= cost:
        profit += cost
        rem = amount - cost
        print(f"Here is $ {round(rem,2)} in change🙂.")
        make_coffee(coffe)
    elif amount <= cost:
        print("Not enough coins🙃, Money refunded")


def check_resource(coffe):
    coffe_ingredients = MENU[coffe]['ingredients']
    for item in coffe_ingredients:
        if resources[item] < coffe_ingredients[item]:
            print(f"Sorry there is no enough {item}😥")
            contd = False
            exit()
    print("Please enter coins.")
    quad_count = int(input("How many Quarters?"))
    dim_count = int(input("How many Dimes?"))
    nic_count = int(input("How many Nickels?"))
    pen_count = int(input("How many Pennies?"))
    calculate(MENU[coffe]["cost"], quad_count, dim_count, nic_count, pen_count, coffe)


contd = True
while contd:
    user_choice = input("What would you like ?(espresso/latte/cappuccino):")
    if user_choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        check_resource(user_choice)
