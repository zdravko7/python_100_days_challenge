from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


running = True
money = 0
drink = None
drink_name = None


while(running):

    operation = input(" What would you like? (espresso/latte/cappuccino):")

    match operation.lower():
        case "off":
          print("Goodbye!")
          running = False
          break
        case 'report':
          coffee_maker.report()
          money_machine.report()
          continue

        case "latte":
          drink_name = 'latte'
        case 'cappuccino':
          drink_name = 'cappuccino'
        case 'espresso':
          drink_name = 'espresso'
        case _ :
          print('Invalid input. Please try again')
          continue

    drink = menu.find_drink(drink_name)

    if not(coffee_maker.is_resource_sufficient(drink)):
       continue

    money_machine.make_payment(drink.cost)

    coffee_maker.make_coffee(drink)

    


    