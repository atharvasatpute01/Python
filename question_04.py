class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, amount):
        if amount > 0:
            self.__price = amount
            print("Price updated successfully")
        else:
            print("Price must be greater than zero!")


m1 = Mobile("Apple", 89999)

print("Brand:", m1.brand)
print("Price:", m1.get_price())

m1.set_price(69999)

print("Updated Price:", m1.get_price())

m1.set_price(0)