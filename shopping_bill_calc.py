def display_items():

    print("\n========== RESTAURANT MENU ==========")
    print("1. Rice          - ₹60/kg")
    print("2. Sugar         - ₹45/kg")
    print("3. Milk          - ₹30/litre")
    print("4. Bread         - ₹40/packet")
    print("5. Biscuits      - ₹20/packet ")
    print("6. Exit")
    print("=====================================")


def get_item_name(choice):

    items = {
        "1": "Rice",
        "2": "Sugar",
        "3": "Milk",
        "4": "Bread",
        "5": "Biscuits"
    }

    return items.get(choice, "Unknown")


def get_price(choice):

    prices = {
        "1": 60,
        "2": 45,
        "3": 30,
        "4": 40,
        "5": 20
    }

    return prices.get(choice, 0)


def calculate_total(cart):

    total = 0

    for item in cart:
        total = total + item["price"] * item["quantity"]

    return total


def print_bill(cart):

    print("\n")
    print("=====================================")
    print("           SHOPPING BILL")
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


def shopping():

    cart = []

    while True:

        display_items()

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


# Start Shopping Bill Calculator
shopping()