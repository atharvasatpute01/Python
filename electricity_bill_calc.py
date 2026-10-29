def calculate_bill(units):

    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    else:
        bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)

    return bill


def display_bill(units, bill):

    print("==============================")
    print("     ELECTRICITY BILL")
    print("==============================")
    print("Units Consumed :", units)
    print("Electricity Bill: ₹", bill)
    print("==============================")


def eleciticity_bill():

    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units.")
        return

    bill = calculate_bill(units)

    display_bill(units, bill)


# Start the program

eleciticity_bill()