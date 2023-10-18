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

def is_resource_sufficient(order_ingredients):
    """Returns true if all good"""
    for item in order_ingredients:
       if (order_ingredients[item] > resources[item]):
          print(f"Sorry there is not enough {item}")
          return False

    return True

def process_coins():
    """Returns the total price of the coins"""
    print('Please insert your coins...')
    quarters = float(input("How many quarters?"))
    dimes = float(input("How many dimes?"))
    nickles = float(input("How many nickles?"))
    pennies = float(input("How many pennies?"))

    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

def use_resources(drink):

    for ingredient in drink["ingredients"]:
       resources[ingredient] -= drink["ingredients"][ingredient]

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
          print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
          continue

        case "latte":
          drink = MENU["latte"]
          drink_name = 'latte'
        case 'cappuccino':
          drnk = MENU['cappuccino']
          drink_name = 'cappuccino'
        case 'espresso':
          drink = MENU['espresso']
          drink_name = 'espresso'
        

    if not(is_resource_sufficient(drink['ingredients'])):
       continue

    totalSum = process_coins()

    #print(totalSum)
    #print(MENU[drink]['cost'])

    #checks if thre is sufficient money
    if (totalSum > drink['cost']):
       print(f'Here is ${round(totalSum - drink["cost"], 2)} dollars in change.')
       money = money + drink['cost']

    use_resources(drink)

    print(f'Here is your {drink_name}. Enjoy!')