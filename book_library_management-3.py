import csv

def load_inventory(filename):   #Make, Model, Year, Price
    dictionary = {}
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        first = True
        for row in reader:
            if first == True:
                first = False
                continue
            make, model, year, price = row
            key = f'{make}_{model}_{year}'
            dictionary[key] = {'Make': make, 'Model': model, 'Year': int(year), 'Price': float('{:.2f}'.format(float(price)))}
    return dictionary

def display_inventory(inventory): 
    for car, details in inventory.items():
        make = details['Make']
        model = details['Model']
        year = details['Year']
        price = details['Price']
        print(f'{make}, {model} {year}: ${price:.2f}')


def update_price(inventory, make, model, year, new_price):
    for car, details in inventory.items():
        if details['Make'] == make and details['Model'] == model and details['Year'] == year:
            details['Price'] = new_price
            return "Price updated successfully"
    return "Vehicle not found in inventory"
        
def sort_by_make(inventory):
    new_dict = dict(sorted(inventory.items(), key = lambda elem: elem[1]['Make']))
    return new_dict

def calculate_price_change(inventory, model):
    for key, dictionary in inventory.items():
        if model == dictionary['Model']:
            make = dictionary['Make']
            year = dictionary['Year']
            price = dictionary['Price']
            if year == 2024:
                print(f'{make}, {model} {year}: ${price:.2f}')
                cost1 = price
            elif year == 2022:
                print(f'{make}, {model} {year}: ${price:.2f}')
                cost2 = price
    try:
        price_change_percentage = ((cost1 - cost2) / cost2) * 100
        return price_change_percentage
    except:
        return 'Not Enough Data to Calculate Price Change!!'
                  
def update_file(new_file, library):
    with open(new_file, mode='w', newline='') as file:
        fieldnames = ['Title', 'Author', 'Year', 'Price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for book in library.values():
            writer.writerow(book)

def update_file(filename, inventory):
    with open(filename, 'w', newline = '') as csvfile:
        fieldnames = ['Make', 'Model', 'Year', 'Price']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for dictionary in inventory.values():
            writer.writerow(dictionary)
def main():
    filename = "vehicle_inventory.csv"
    inventory = load_inventory(filename)
    while True:
        
        print("\nMENU:")
        print("1. Display Inventory")
        print("2. Update Vehicle Price")
        print("3. Sort Inventory by Make")
        print('4. Calculate Price Changes')
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_inventory(inventory)

        elif choice == '2':
            make = input("Enter the make of the car:")
            model = input("Enter the model of the car:")
            year = int(input('Enter the year of the car:'))
            new_price = float(input("Enter the new price: "))
            new_file = input('Enter a file name:')
            print(update_price(inventory, make, model, year, new_price))
            update_file(new_file, inventory)
            
        elif choice == '3':
            inventory = sort_by_make(inventory)
    
        elif choice == '4':
            model = input('Enter the model of the car:')
            print(calculate_price_change(inventory, model))
        
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
main()
