# Name: Alisha Gursahaney
# Net Id: amg9zd

# Partner: Sophia Cheng szc8bkk

roots_menu = {"El Jefe": 9.85, "The Southern": 8.85, "The Apollo": 9.35}
got_dumplings_menu = {"Chicken dumplings": 4.95, "Original Ramen": 10.50, "Thai Milk Tea": 4.50, "Edamame": 3.50}
all_cville_restaurants = {"Roots": roots_menu, "Got Dumplings": got_dumplings_menu}


def add_menu_item(dictionary, new_menu_item, item_price):
    dictionary[new_menu_item] = item_price


add_menu_item(roots_menu, "Roots Bowl", 8.35)


def calculate_order(menu, order_list, tip=0.18):
    order_sum = 0
    for order in order_list:
        if order in menu:
            order_sum += menu[order]
        else:
            print(f"The {order} is unavailable")
            new_item = input("Please order a different item: ")
            while order not in order_list:
                print(f"The {order} is unavailable")
                new_item = input("Please order a different item: ")
            order_sum += menu[new_item]
    total = order_sum + (tip * order_sum) + (0.06 * order_sum)
    total = round(total, 2)
    return total


def print_the_menu(dictionary):
    for menu_item in dictionary:
        print(f"{menu_item} - ${dictionary[menu_item]}")


def place_mega_order(mega_menu, order):
    total = 0
    for restaurant in order:
        if restaurant in mega_menu:
            menu_total = calculate_order(mega_menu[restaurant], order[restaurant])
            total += menu_total
        else:
            print(f"That {restaurant} is unavailable")
    return total


print(place_mega_order(all_cville_restaurants,
                       {"Roots": ["El Jefe", "The Apollo"], "Got Dumplings": ["Original Ramen", "Edamame"]}))


print(calculate_order(roots_menu, ["El Jefe", "Bowl"]))
