from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True

while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if CoffeeMaker.off(choice):
        on = False
        print("Never come back, you human!!")
    else:
        if choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            if menu.find_drink(choice):
                if coffee_maker.is_resource_sufficient(menu.find_drink(choice)) \
                        and money_machine.make_payment(menu.find_drink(choice).cost):
                    coffee_maker.make_coffee(menu.find_drink(choice))

