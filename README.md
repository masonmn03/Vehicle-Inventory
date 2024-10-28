This project is a Python-based command-line application for managing a vehicle inventory. It loads vehicle data from a CSV file, allowing users to display, update, and sort vehicles as well as calculate price changes over time.

Features:

	Load Inventory: Load vehicle data from a CSV file with columns for Make, Model, Year, and Price.

	Display Inventory: Display all vehicle records in the inventory with formatted details.

	Update Price: Update the price of a specific vehicle in the inventory.

	Sort by Make: Sort the inventory alphabetically by vehicle make.

	Calculate Price Change: Calculate the percentage change in price for a vehicle model between the most recent and previous years.

Installation:

Prerequisites:

  1. Python 3
	
  2. Download vehicle_inventory.csv (CSV file containing vehicle data with Make, Model, Year, and Price columns)
	
  3. Make sure the csv file is in the same directory as your pyfile.

Functions:

  - load_inventory(filename): Loads the inventory data from a specified CSV file.
	
  - display_inventory(inventory): Displays each vehicle in the inventory with formatted details.
	
  - update_price(inventory, make, model, year, new_price): Updates the price of a specified vehicle.
	
  - sort_by_make(inventory): Sorts the inventory alphabetically by make.
	
  - calculate_price_change(inventory, model): Calculates the price change percentage between years for a specified model.
	
  - update_file(filename, inventory): Writes the updated inventory data back to the CSV file.

Thank you for checking out this project! 
