sp= int(input("enter selling price: "))
cp= int(input("enter cost price: "))
qty= int(input("enter the quantity: "))

profit = (sp-cp)*qty
print(f"The profit is {profit}")

profit_percentage= profit/(cp*qty)
print(f"The profit_percentage is {profit_percentage}")

