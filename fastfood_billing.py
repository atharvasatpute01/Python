# Simple Restaurant Billing System


def display_menu():
    print("\n========== RESTAURANT MENU ==========")
    print("1. Pizza       - ₹250")
    print("2. Burger      - ₹150")
    print("3. Pasta       - ₹200")
    print("4. Sandwich    - ₹100")
    print("5. Coffee      - ₹80")
    print("6. Exit")
    print("=====================================")


def get_price(choice):

    prices = {
        "1": 250,
        "2": 150,
        "3": 200,
        "4": 100,
        "5": 80
    }

    return prices.get(choice, 0)


def get_item_name(choice):

    items = {
        "1": "Pizza",
        "2": "Burger",
        "3": "Pasta",
        "4": "Sandwich",
        "5": "Coffee"
    }

    return items.get(choice, "Unknown")


def calculate_total(cart):

    total = 0

    for item in cart:
        total = total + item["price"] * item["quantity"]

    return total


def print_bill(cart):

    print("\n")
    print("=====================================")
    print("          RESTAURANT BILL")
    print("=====================================")

    for item in cart:

        amount = item["price"] * item["quantity"]

        print(
            item["name"],
            "x",
            item["quantity"],
            "=",
            "₹" + str(amount)
        )

    total = calculate_total(cart)

    print("-------------------------------------")
    print("Total Amount: ₹", total)
    print("=====================================")


def restaurant():

    cart = []

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "6":
            break

        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice!")
            continue

        quantity = int(input("Enter quantity: "))

        item = {
            "name": get_item_name(choice),
            "price": get_price(choice),
            "quantity": quantity
        }

        cart.append(item)

        print(
            item["name"],
            "added to your order."
        )

    if len(cart) > 0:
        print_bill(cart)

    else:
        print("No items ordered.")

    print("Thank you! Visit again.")


# Start Restaurant Billing System
restaurant()