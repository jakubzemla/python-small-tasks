from source_data import MENU, resources

# === DEFAULT SETTINGS === #
item_match = False
price = dict()
for item in MENU.keys():
    price[item] = MENU[item]["cost"]


# === FUNCTIONS === #

def report(rsc):
    for key, value in rsc.items():
        print(f"{key}: {value}")

def insert_coins(choice, total = 0):
    print("Please insert coins 1, 2, 5, 10, 20, 50")
    coins = [1, 2, 5, 10, 20, 50]
    for coin in coins:
        if total >= price[choice]:
            print(f"You have inserted a total {total} coins.") 
            break
        total += int(input(f"How many {coin}-coins want to insert? ")) * coin
        print(f"Your current amount is {total} coins. For the {choice} you need {price[choice]} coins.")
    if total < price[choice]:
        print(f"Not enough coins. You still need to insert {price[choice] - total} coins.")
        return insert_coins(choice, total)
    else:
        return total

def calculate_change(user_amount, item_price):
    refund = user_amount - item_price
    if refund >= 0:
        print("Your coffee is being prepared.")
        if refund > 0:
            print(f"Here is your change: {refund} coins.")

def fill_in_resources():
    return resources

def consumption_of_resources(choice):
    for source in rest_of_resources:
        rest_of_resources[source] -= MENU[choice]["ingredients"][source]

def control_resources(rsc, drink):
    for source in rsc.keys():
        if rsc[source] < MENU[drink]["ingredients"][source]:
            print(f"Not enough ingredients. Please fill the {source}.")
            quit()

# === COFFEE MACHINE CODE === #
rest_of_resources = fill_in_resources()
next_drink = True

while next_drink:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "report":
        report(rest_of_resources)

    control_resources(rest_of_resources, user_choice)

    for key in MENU.keys():
        if user_choice == key:
            item_match = True
            print(f"The {user_choice} costs {price[user_choice]} coins.")
            amount = insert_coins(user_choice, 0)
            calculate_change(amount, price[user_choice])
            consumption_of_resources(user_choice)
            print(rest_of_resources)
    if not item_match:
        print(f"Your choice '{user_choice}' is not in MENU list. Let's start again.") 
        quit()
    next_one = input("Would you like to order another coffee? Type 'yes' or 'no: ")
    if next_one != "yes":
        next_drink = False