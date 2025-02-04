
menu = {
    'pizza': 60,
    'burger': 55,
    'pasta': 70,
    'fries': 30,
    'coke': 20,
    'sandwich': 45,
}


print('Welcome to the my restaurant')
print('pizza: Rs.60\nburger: Rs.55\npasta: Rs.70\nfries: Rs.30\ncoke: Rs.20\nsandwich: Rs.45\n')

order_total  = 0

item_1 = input('Enter your order: ')
if item_1 in menu:
    order_total += menu[item_1]
    print(f'Your item {item_1} added to your order')

else:
    print(f"Sorry, we don't have {item_1} in our menu")

while True:
    another_oder = input('Do you want to order another item? (yes/no): ')
    if another_oder == 'yes':
        item_2 = input('Enter your order: ')
        if item_2 in menu:
            order_total += menu[item_2]
            print(f'Your item {item_2} added to your order')

        else:
            print(f"Sorry, we don't have {item_2} in our menu")

    else:
        break

print(f'Your total order amount is: Rs.{order_total}')

