from coffeMachineAssets import *


# Main function of the program. This function mimics the basics of a coffee machine functionalities.
def machine_menu():
    """
        :Receives nothing.
        :return: nothing.
    """
    logo()
    has_costumer = True
    products = {"water": 500, "milk": 500, "coffee": 500}
    machine_money = 0.0

    while has_costumer:

        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_input in MENU:
            if has_ingredients(products, user_input):
                print("Please insert coins.")
                machine_money += take_money(user_input, products)
            else:
                missing_ingredients(products, user_input)
        elif user_input == "off":
            has_costumer = False
        elif user_input == "report":
            machine_report(products, machine_money)
        else:
            print("The machine does not have this order!")

        if not has_costumer:
            print("Bye, bye!")


# Printing the machine report
def machine_report(products, money):
    """
        :param products: dict
        :param money: float
        :return: nothing
    """
    print(f"Water: {products['water']}ml")
    print(f"Milk: {products['milk']}ml")
    print(f"Coffee: {products['coffee']}ml")
    print(f"Money: ${'{:.2f}'.format(round(money, 2))}")


# Checking the machine's resources
def has_ingredients(products, recipe):
    """
        :param products: dict
        :param recipe: string
        :return: boolean
    """
    water_needed = MENU[recipe]["ingredients"]["water"]
    milk_needed = MENU[recipe]["ingredients"]["milk"]
    coffee_needed = MENU[recipe]["ingredients"]["coffee"]

    if products["water"] >= water_needed and products["milk"] >= milk_needed and products["coffee"] >= coffee_needed:
        return True
    return False


# Printing the missing ingredients in the machine for the user.
def missing_ingredients(products, recipe):
    """
        :param products: dict
        :param recipe: string
        :return: nothing
    """
    water_needed = MENU[recipe]["ingredients"]["water"]
    milk_needed = MENU[recipe]["ingredients"]["milk"]
    coffee_needed = MENU[recipe]["ingredients"]["coffee"]

    if products["water"] < water_needed:
        print(f"Sorry there is not enough water. {water_needed - products['water']}ml")

    if products["milk"] < milk_needed:
        print(f"Sorry there is not enough milk. {milk_needed - products['milk']}ml")

    if products["coffee"] < coffee_needed:
        print(f"Sorry there is not enough coffee. {coffee_needed - products['coffee']}ml")


# Checking if the user money is enough to buy
def has_money(recipe, money):
    """
      :param recipe: string
      :param money: float
      :return: boolean
    """
    if money >= MENU[recipe]["cost"]:
        return True
    return False


# Process coins
def convert_value(quarters, dimes, nickles, pennies):
    """
        :param quarters: integer
        :param dimes: integer
        :param nickles: integer
        :param pennies: integer
        :return: float
    """
    return round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01)


# Checking if the transaction is successful
def take_money(recipe, products):
    """
        :param recipe: string
        :param products: dict
        :return: float
    """
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_value = convert_value(quarters, dimes, nickles, pennies)

    if has_money(recipe, total_value):
        change = total_value - MENU[recipe]["cost"]
        print(f"Here is {'{:.2f}'.format(round(change, 2))} in change.")
        make_recipe(recipe, products)
        return MENU[recipe]["cost"]

    print(f"Sorry that's not enough money. Money refunded.")
    return 0.0


# Making the products
def make_recipe(recipe, products):
    """
        :param recipe: string
        :param products: dict
        :return: nothing
    """
    if recipe == "espresso":
        print('''Here is your espresso ☕️. Enjoy!''')
    elif recipe == "latte":
        print('''Here is your latte ☕️. Enjoy!''')
    elif recipe == "cappuccino":
        print('''Here is your cappuccino ☕️. Enjoy!''')

    products["water"] -= MENU[recipe]["ingredients"]["water"]
    products["milk"] -= MENU[recipe]["ingredients"]["milk"]
    products["coffee"] -= MENU[recipe]["ingredients"]["coffee"]


# Calling the main function
machine_menu()
