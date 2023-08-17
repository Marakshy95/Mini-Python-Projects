MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def cost_calculator(quarters):

    total_paid = float(quarters) * 0.25
    total_cost = float(MENU[f"{user_answer}"]["cost"])

    while total_paid < total_cost:
        total_change_reversed = total_cost - total_paid
        print(f"you paid a total of ${total_paid} you still need to pay ${total_change_reversed}")
        total_paid += (float(input("How many more quarters are you adding?")) * 0.25)

    total_change = total_paid - total_cost
    print(f"You paid a total of ${total_paid}")
    print(f"Your total cost is ${total_cost}")
    print(f"Here is ur change of {total_change}")



def main():
    if user_answer == "off":
        quit()
    elif user_answer == "report":
        print(resources)
    
    if water_cost > current_water:
        print(f"Not enough maya for {user_answer}, please order something else.")
        print(resources)
    elif coffee_cost > current_coffee:
        print(f"Not enough coffee for {user_answer}, please order something else.")
        print(resources)
    elif milk_cost > current_milk:
        print(f"Not enough melk for {user_answer}, please order something else.")
        print(resources)
    else:
        print(f"Here is your {user_answer}, Enjoy!!!")
        resources["water"] =  current_water - water_cost
        resources["coffee"] =  current_coffee - coffee_cost
        resources["milk"] = current_milk - milk_cost
        print(resources)




# To keep the program running and turns off if false
x = True

while x == True:

    user_answer = input("What would you like? An espresso / latte or cappuccino? ")

    water_cost = MENU[f"{user_answer}"]["ingredients"]["water"]
    coffee_cost = MENU[f"{user_answer}"]["ingredients"]["coffee"]
    milk_cost = MENU[f"{user_answer}"]["ingredients"]["milk"]

    current_water = resources["water"]
    current_coffee = resources["coffee"]
    current_milk = resources["milk"]
    
    if current_water <= 0 or current_coffee <= 0 or current_milk <= 0:
        print("Please Refill the water")
        quit()
    else:
        main()
        number_of_quarters = input("How many quarters? ")
        cost_calculator(number_of_quarters)