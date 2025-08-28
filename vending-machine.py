#The script sells multiple products. The user might buy more than 1 product and more than 1 unit of each product.
#At the end, the script shows the total amount to pay.

products = {
"Coca-Cola": 1.50,
"Sprite": 2.00,
"Water": 1.25,
"Sparkling Water": 1.25,
"Potato Chips": 1.75,
"Chocolate": 1.00
}

def choose_product():
    choose_product = int(input("Insert the number of the item you would like to buy:"))
    choose_amount = int(input(f"Insert how many would like to buy:"))
    product, price = list(products.items()) [choose_product-1]
    total_item = price * choose_amount
    print (total_item)
    return total_item

purchase = input("Would you like to buy a drink? Type 'Yes' or 'No'")


if purchase in ['yes','Y','y']:
    print("Ok!")
    total_bought = 0
    while True:
        for index, (name, price) in enumerate(products.items(), start = 1):
            print(f"{index} - {name}:${price:.2f}")
        machine_option = choose_product()
        total_bought += machine_option
        buy_more = input("Would you like to buy more products? (Y/N)")
        if buy_more not in ['yes','Y','y']:
            print(f"Your total is: ${total_bought:.2f}")
            break

elif purchase in ['no','N','n']: 
    print("Ok, have a nice day")
    
else:
    print("No valid option. Try again")


                 
