import data

playCoffeeGame = True
resources = data.resources
menu = data.MENU
money = 0

def transaction(choose, coint):
    # TODO 4: Do a transaction
        print("Please insert your count")
        quarters = int(input('How many quarters?: '))
        dimes = int(input('How many dimes?: '))
        nickles = int(input('How many nickles?: '))
        pennies = int(input('How many pennies?: '))
        monetary = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)
        print(monetary)
        if monetary < coint:
            print("Sorry that's nor enough money. Money refunded.")
            return False
        else :
            change = round(monetary - coint, 2)
            print(f"Here is ${change} in change")
            print(f"Here is your {choose} ☕. Enjoy!")
            return True

def restResources(choose):
    # TODO 2: import the information of choose
    water = menu[choose]['ingredients']['water']
    coffee = menu[choose]['ingredients']['coffee']
    cost = menu[choose]['cost']
    if choose == "espresso":
        milk = 0
    else :
        milk = menu[choose]['ingredients']['milk']
    
    # TODO 3: check the resources
    print(water)
    print(resources['water'])
    print(water > resources['water'])
    if water > resources['water']:
        print("Sorry there is not enough water")
        return False
    elif coffee > resources['coffee']:
        print("Sorry there is not enough coffee")
        return False
    elif milk > resources['milk']:
        print("Sorry there is not enough milk")
        return False
    else:
        if transaction(choose, cost):
            global money
            money = menu[choose]['cost']
            resources['water'] = resources['water'] - water
            resources['coffee'] = resources['coffee'] - coffee
            resources['milk'] = resources['milk'] - milk

    
while playCoffeeGame:
    choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO 1: Check choose of user
    if choose == "off":
        playCoffeeGame = False
    elif choose == "report":
        print(f"|Water: {resources['water']}\n|Milk: {resources['milk']}\n|Coffee: {resources['coffee']}\n|Money: ${money}")
    elif choose not in ["espresso", "latte", "cappuccino", "off", "report"] :
        print("Please enter a valide choose")
    else :
        restResources(choose)