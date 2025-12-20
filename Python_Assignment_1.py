inventory = {
    '101': ['Laptop', 18, 49000],
    '102': ['Phone', 23, 12000],
    '103': ['Speaker', 10, 4500],
    '104': ['Cell Phone', 15, 9000]
}

bill_items = []  
total_qty = 0
total_amount = 0

print("Enter item details (type 'done' to finish):")

while True:
    item_code = input("Item code: ")

    if item_code.lower() == 'done':
        break

    if item_code not in inventory:
        print("Invalid item code!")
        continue

    qty = int(input("Qty: "))

    if qty > inventory[item_code][1]:
        print("Insufficient stock!")
        continue

   
    inventory[item_code][1] -= qty

    item_name = inventory[item_code][0]
    price = inventory[item_code][2]
    amount = qty * price

    bill_items.append([item_name, qty, amount])
    total_qty += qty
    total_amount += amount


print("\n=========================================")
print("        ABC ELECTRONICS MART")
print("=========================================")
print("SNO   ITEM NAME           QTY     PRICE")
print("-----------------------------------------")

for i, item in enumerate(bill_items, start=1):
    print(f"{i:<5} {item[0]:<18} {item[1]:<7} {item[2]}")

print("-----------------------------------------")
print(f"      TOTAL               {total_qty:<7} {total_amount}")
