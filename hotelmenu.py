#Define the menu of restaurant

menu = {
    "pizza":50,
    "burger":30,
    "pasta":40, 
    "Salad":70,
    "Coffee":80,
    "tea":20, 
    "samosa":10, 
}

#Function to display the menu

print("Welcome to the hotel")
print("pizza: tk 50\nburger: tk 30\npasta: tk 40\nSalad: tk 70\nCoffee: tk 80\ntea: tk 20\nsamosa: tk 10 ")

order_total = 0
#50+30+40+70+80+20+10 = 300

item_1 = input("Enter the name of the item you want to order:")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your order item is {item_1} and the price is {menu[item_1]}")
else:
    print(f"Sorry, {item_1} is not availabole in the menu.")

another_item = input("Do you want to order another item? (yes/no)")
if another_item == "yes":
    item_2 = input("Enter the name of the item you want second to order:") 
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your order item is {item_2} and the price is {menu[item_2]}")
    else:
        print(f"Sorry, {item_2} is not availabole in the menu.")

print(f"Your total order is {order_total} tk ")
