stock = {"itemA": 0, "itemB": 5, "itemC": 20, "itemD": 8}

# Remove items with 0 stock
stock = {k:v for k,v in stock.items() if v > 0}

# Restock items below 10 (+50 units)
for k, v in stock.items():
    if v < 10:
        stock[k] += 50

# Total inventory
total_inventory = sum(stock.values())

print("Updated Stock:", stock)
print("Total Inventory Count:", total_inventory)