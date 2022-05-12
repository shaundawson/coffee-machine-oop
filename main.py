from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "off":
        is_on = False
    # TODO Print report.
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # TODO Check resources sufficient?
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            # TODO Check transaction successful?
            if money_machine.make_payment(drink.cost):
                # TODO Make Coffee.
                coffee_maker.make_coffee(drink)






