# *Online Shopping Bill*

# Objective

# Create an Online Shopping Billing System.

# --------------------------------
# Online Shopping Billing System
# --------------------------------


# Global Variable : store_name

store_name = "unique_mart"

# Customer Details : Customer Name, Mobile Number, City

customer_name = "Atharva Satpute"

mobile_number = 8282899999

city = "Kolhapur"


# Store prices of : Laptop, Mouse, Keyboard, Headphones, Pen Drive (Multiple Assignment)

laptop_price, mouse_price, keyboard_price, headphones_price, pendrive_price = 60000, 1200, 2500, 3500, 800

# Calculate : Total Bill

total_bill = laptop_price + mouse_price + keyboard_price + headphones_price + pendrive_price


# Swapping two variables : Laptop Price and Mouse Price

# Before Swapping :
 
print("\n----- Before Swapping -----")

print(f"Laptop Price : {laptop_price}")

print(f"Mouse Price : {mouse_price}")

# Swapping Variables :

laptop_price, mouse_price = mouse_price, laptop_price

# After Swapping :

print("\n----- After Swapping -----")

print(f"Laptop Price : {laptop_price}")

print(f"Mouse Price : {mouse_price}")


# Display output using f-strings.

print("\n==============================")
print("ONLINE SHOPPING BILLING SYSTEM")
print("==============================")


print(f"\nStore Name : {store_name}")

# Display Customer Information :

print(f"\nCustomer Name : {customer_name}")

print(f"Mobile Number : {mobile_number}")

print(f"City : {city}")

# Display Bill :

print("\n------ Bill ------")

print(f"Laptop : {laptop_price}")

print(f"Mouse : {mouse_price}")

print(f"Keyboard : {keyboard_price}")

print(f"Headphones : {headphones_price}")

print(f"Pendrive : {pendrive_price}")

# Display Total Bill :

print("\n------ Total Bill ------")

print(f"Total Bill : {total_bill}")

print("\n-------- Thanks for visiting... --------")