import random

def daily_sales(available_items, inventory_records, current_day):

    if current_day % 7 != 0:    # Checks if day is not equal to 7 (the restock day)
        sold_units = random.randrange(0,200)    # Creates a random value between 0 and 200 to use at the sold units for the day
        available_items = available_items - sold_units  # Amends available_items after items have been sold
        inventory_records.append([current_day, sold_units, 0, available_items]) # Appends the new infomation onto inventory_records
    
    return available_items