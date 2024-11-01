from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee = CoffeeMaker()
money = MoneyMachine()
coffee_menu = Menu()


while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino/):\n").lower()
    if user_input == "report":
        coffee.report()
        money.report()
    elif user_input == "off":
        print("Shutting down!")
        is_on = False
    else:
        coffee_choice = coffee_menu.find_drink(user_input)
        if coffee_choice is not None:
             if coffee.is_resource_sufficient(coffee_choice):
                coffee_cost = coffee_choice.cost
                if money.make_payment(coffee_cost):
                    coffee.make_coffee(coffee_choice)

        else:
            print("Please select from options provided")


