from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
cm = CoffeeMaker()
mc = MoneyMachine()

is_on = True


while is_on:
    user_input = input(f"What would you like to drink {menu.get_items()} ?! ")
    if user_input == "report":
        print("Here are ur current stats \n ")
        print(cm.report())
    elif user_input == "off":
        print("Goodbye!")
        quit()
    else:
        drink = menu.find_drink(user_input)
        print("Insert Coins")
        cost = mc.make_payment(drink.cost)
        if cm.is_resource_sufficient(drink) and cost:
            cm.make_coffee(drink)

