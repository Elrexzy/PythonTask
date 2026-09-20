name = input("Enter a name: ")
print(name)

user_option_one = "yes"
total = 0

while user_option_one == "yes":

    product_name = input("Enter the product name: ")
    print(product_name)

    quantity_of_product = int(input("Enter the quantity of " + product_name + " : "))
    print(quantity_of_product)

    price_of_product = float(input("Enter the price of " + product_name + " : "))
    print(price_of_product)

    amount = quantity_of_product * price_of_product
    total += amount

    print("Current total:", total)

    user_option_one = input("Add another product Yes/No: ").lower()

else:
    print("Thank you for your services")
    print("Final total:", total)
