from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffer_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on: 
    choose = input(f"What would you like? ({menu.get_items()})): ").lower()
    if choose == "report":
        coffer_maker.report()
        money_machine.report()
    elif choose == "off":
        is_on = False
    else:
        drink = menu.find_drink(choose)
        if drink:
            if coffer_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffer_maker.make_coffee(drink)
            else:
                print("The ressorces is already finished")
        else:
            print("Please enter a valide choose")