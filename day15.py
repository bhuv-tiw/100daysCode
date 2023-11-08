coffee_machine = {
    "milk": 200,
    "coffee": 100,
    "water": 300,
    "Money": 0
}
requirements = {
    "espresso": {
        "milk": 0,
        "water": 50,
        "coffee": 18,
        "Money": 1.50
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "Money": 2.50
    },
    "capucinno": {
        "water": 250,
        "milk": 24,
        "coffee": 100,
        "Money": 3.00

    }
}
coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}
while input("would you like espresso, latte or capucinno?"):
    user_choice=input("Enter your choice")
    if user_choice == "report":
        print(
            f"milk : {coffee_machine["milk"]}ml\ncoffee : {coffee_machine["coffee"]}g\nwater : {coffee_machine["water"]}ml\nMoney : {coffee_machine["Money"]}$")
    else:
        val = True
        for keys, values in coffee_machine.items():
            if coffee_machine[keys] < requirements[user_choice][keys] and keys != "Money":
                val = False
                print("sorry insufficient {keys}")
                break
        if val:
            print("please insert coins")
            penny = int(input("how many penny"))
            nickel = int(input("how many nickel"))
            dime = int(input("how many dime"))
            quarter = int(input("how many quarter"))
            total_money = penny * coins["penny"] + nickel * coins["nickel"] + dime * coins["dime"] + quarter * coins[
                "quarter"]
            cost = requirements[user_choice]["Money"]
            print(f"here is your change of {total_money - cost}")
            print(f"Enjoy your {user_choice}")
            coffee_machine["milk"] -= requirements[user_choice]["milk"]
            coffee_machine["coffee"] -= requirements[user_choice]["coffee"]
            coffee_machine["water"] -= requirements[user_choice]["water"]
            coffee_machine["Money"] += requirements[user_choice]["Money"]

