#Define the menu of restaurant
#from pandas.conftest import ordered

menu = {
    'Pizza': 90,
    'Manchurin':50,
    'Burger':40,
    'Paneer Tikka':80,
    'Coffee':100
}


#Greet
print('Welcome to Pahadi Restaurant')
print('Pizza: Rs40\nManchurin: Rs50\nBurger: Rs50\nPaneer Tikka: Rs80\nCoffee: Rs70\n')


order_total = 0
#70+60 =130
item_1 = input('Enter the name of item you want to order =')
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f'your item {item_1} has been added to you order')

else:
    print(f'Ordered item {item_1}is not available yet')

another_order = input('Do you want to add another item? (Yes/No)')
if another_order == 'yes':
    item_2 = input('Enter the name of secon item = ')
    if item_2 in menu:
        order_total += menu[item_2]
        print(f'Item {item_2} has been addded to order')
    else:
        print(f'Ordered item {item_2} is not available!')
print(f'The total amount of items to pay is {order_total}')

