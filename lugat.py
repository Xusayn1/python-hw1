import json
import os


SHOP_DATA_FILE = "shop_data.json"

def load_shop_data():

    if os.path.exists(SHOP_DATA_FILE):
        try:
            with open(SHOP_DATA_FILE, 'r', encoding='utf-8') as file:
                data = json.load(file)

                return {int(k): v for k, v in data.items()}
        except (json.JSONDecodeError, KeyError, ValueError):
            print("Error reading shop data file. Starting with empty shop.")
            return {}
    else:
        print("Shop data file not found. Starting with empty shop.")
        return {}


def save_shop_data(shop_data):

    try:
        with open(SHOP_DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(shop_data, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving shop data: {e}")
        return False


def view_shop_all_items(thing: dict):

    print("\n--- All Items in Shop ---")
    if not thing:
        print("No items in shop")
        return

    for k, v in thing.items():
        print(f'id {k}. title: {v["title"]}, price: {v["price"]}, year: {v["year"]}, type: {v["type"]}')


def view_phone(thing: dict):

    print("\n--- Phones ---")
    found = False
    for k, v in thing.items():
        if v["type"].lower() == 'phone':
            print(f'id {k}. title: {v["title"]}, price: {v["price"]}, year: {v["year"]}')
            found = True
    if not found:
        print("No phones found in shop")


def view_tv(thing: dict):

    print("\n--- TVs ---")
    found = False
    for k, v in thing.items():
        if v["type"].lower() == 'tv':
            print(f'id {k}. title: {v["title"]}, price: {v["price"]}, year: {v["year"]}')
            found = True
    if not found:
        print("No TVs found in shop")


def view_pc(thing: dict):

    print("\n--- PCs ---")
    found = False
    for k, v in thing.items():
        if v["type"].lower() == 'pc':
            print(f'id {k}. title: {v["title"]}, price: {v["price"]}, year: {v["year"]}')
            found = True
    if not found:
        print("No PCs found in shop")


def add_thing_to_shop(thing: dict):

    print("\n--- Add New Item ---")
    title = input("Enter title: ")
    price = input("Enter price: ")
    year = input("Enter year: ")
    item_type = input("Enter type: ")

    new_id = max(thing.keys()) + 1 if thing else 1

    thing[new_id] = {
        "title": title,
        "price": price,
        "year": year,
        "type": item_type
    }

    if save_shop_data(thing):
        print('Item added successfully to shop and saved to file!')
    else:
        print('Item added to current session but failed to save to file!')


def delete_item_from_shop(thing: dict):

    print("\n--- Delete Item ---")
    view_shop_all_items(thing)

    if not thing:
        return

    try:
        item_id = int(input("Enter the ID of item to delete: "))
        if item_id in thing:
            deleted_item = thing.pop(item_id)
            if save_shop_data(thing):
                print(f'Item "{deleted_item["title"]}" deleted successfully!')
            else:
                print("Error saving changes to file!")
        else:
            print("Item ID not found!")
    except ValueError:
        print("Please enter a valid number!")




def manager_for_shop():
    shop_data = load_shop_data()

    while True:
        print("\n" + "=" * 50)
        print("=== SHOP MANAGEMENT SYSTEM ===")
        print("=" * 50)
        options = input(
            '1. See all items in shop\n2. See group of items\n3. Add new item\n4. Delete item\n5. Exit\nChoose your option: ')

        if options == '1':
            while True:
                kod = input('\n1. View all things\n2. Return to main menu\nChoose your option: ')
                if kod == '1':
                    view_shop_all_items(shop_data)
                elif kod == '2':
                    break
                else:
                    print("Invalid option, please try again")

        elif options == '2':
            while True:
                kod2 = input(
                    '\n1. Phone section\n2. TV section\n3. PC section\n4. Return to main menu\nChoose your option: ')
                if kod2 == '1':
                    view_phone(shop_data)
                elif kod2 == '2':
                    view_tv(shop_data)
                elif kod2 == '3':
                    view_pc(shop_data)
                elif kod2 == '4':
                    break
                else:
                    print("Invalid option, please try again")

        elif options == '3':
            add_thing_to_shop(shop_data)

        elif options == '4':
            delete_item_from_shop(shop_data)


        elif options == '5':
            print("Exiting shop management system...")
            break

        else:
            print("Invalid option, please try again")




manager_for_shop()