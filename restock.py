def restock_inventory(available_items, inventory_records, current_day):

    if current_day % 7 == 0:    # Checks if current day is a 7th day of the week
        restocked_units = (2000-available_items)    # Sees how many items need to be restocked
        available_items = 2000  # Restocks available_items by setting it to 2000
        inventory_records.append([current_day, 0, restocked_units, available_items])    # Appends new data to inventory_records
    
    return available_items