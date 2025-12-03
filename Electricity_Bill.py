prev_reading = int(input("Enter the previous Reading: "))
current_reading =int(input("Enter the current Reading: "))

total_consumption = current_reading - prev_reading 
print(f"The current month units are {total_consumption}")
slab_1, slab_2, slab_3, slab_4, slab_5, slab_6 = 50, 100, 200, 300, 400, 800
Free_Slab=200
if total_consumption<0:
    print("Invalid Number!!")
elif total_consumption <= Free_Slab:
    amount =0
else:
    amount =10
    print("select the Meter Type: ")
    print("Enter 1 for single phase upto 1kW")
    print("Enter 2 for single phase above 1kW")
    print("Enter 3 for Three phase")
    meter_type= input("Enter the number here: ")
    if meter_type == "1":
        amount+= 25
    elif meter_type =="2":
        amount += 50
    elif meter_type =="3":
        amount += 150
    else:
        print("Invalid Number and it assumes as 3")
        amount+=150

Rate_1, Rate_2, Rate_3, Rate_4, Rate_5, Rate_6, Rate_7= 1.95, 3.10, 4.80, 7.70, 9.00, 9.50, 10.00
# SLAB:1) 0-50 units = 50
if total_consumption <= slab_1:
    amount += total_consumption*Rate_1
# SLAB:2)  51-100 units = 50
elif total_consumption <= slab_2:
    amount+= (slab_1 * Rate_1) + (total_consumption - slab_1) * Rate_2
# SLAB:3)  100-200 units = 100
elif total_consumption<= slab_3:
    amount+= (slab_1 * Rate_1) + (slab_1 * Rate_2) + (total_consumption - slab_2) * Rate_3
# SLAB:4)  201-300 units = 100
elif total_consumption <= slab_4:
    amount+= (slab_1 * Rate_1) + (slab_1 * Rate_2) + (slab_1 * Rate_3) + (total_consumption - slab_3) * Rate_4
# SLAB:5)  301-400 units = 100
elif total_consumption <= slab_5:
    amount+= (slab_1 * Rate_1) + (slab_1 * Rate_2) + (slab_2 * Rate_3) + (slab_2 * Rate_4) + (total_consumption - slab_4) * Rate_5
# SLAB:6)  401-800 units = 400
elif total_consumption <= slab_6:
    amount+= (slab_1 * Rate_1) + (slab_1 * Rate_2) + (slab_2 * Rate_3) + (slab_2 * Rate_4) + (slab_2 * Rate_5) + (total_consumption - slab_6) * Rate_6
#  SLAB:7) More than 800
else:   
    amount+= (slab_1 * Rate_1) + (slab_2 * Rate_2) + (slab_2 * Rate_3) + (slab_2 * Rate_4) + (slab_2 * Rate_5) + (slab_6 * Rate_6) + (total_consumption-800) * Rate_7

print(f"The Total Amount is {amount}")



# ---------------------------------------------------------------------------- #

#NUMBERS



prev_reading = int(input("Enter the previous Reading: "))
current_reading = int(input("Enter the current Reading: "))

# Correct formula
total_consumption = current_reading - prev_reading

# First check validity
if total_consumption < 0:
    print("Invalid Number!!")
    exit()

print(f"The current month units are {total_consumption}")

# Meter charges
if total_consumption <= 200:
    amount = 0
else:
    amount = 10
    print("Select the Meter Type: ")
    print("1 - Single phase upto 1kW")
    print("2 - Single phase above 1kW")
    print("3 - Three phase")

    meter_type = input("Enter the number here: ")

    if meter_type == "1":
        amount += 25
    elif meter_type == "2":
        amount += 50
    elif meter_type == "3":
        amount += 150
    else:
        print("Invalid number, assuming 3")
        amount += 150

# SLAB CALCULATION
if total_consumption <= 50:
    amount += total_consumption * 1.95
elif total_consumption <= 100:
    amount += (50 * 1.95) + (total_consumption - 50) * 3.10
elif total_consumption <= 200:
    amount += (50 * 1.95) + (50 * 3.10) + (total_consumption - 100) * 4.80
elif total_consumption <= 300:
    amount += (50 * 1.95) + (50 * 3.10) + (100 * 4.80) + (total_consumption - 200) * 7.70
elif total_consumption <= 400:
    amount += (50 * 1.95) + (50 * 3.10) + (100 * 4.80) + (100 * 7.70) + (total_consumption - 300) * 9.00
elif total_consumption <= 800:
    amount += (50 * 1.95) + (50 * 3.10) + (100 * 4.80) + (100 * 7.70) + (100 * 9.00) + (total_consumption - 400) * 9.50
else:
    amount += (50 * 1.95) + (50 * 3.10) + (100 * 4.80) + (100 * 7.70) + (100 * 9.00) + (400 * 9.50) + (total_consumption - 800) * 10.00

print(f"Total Amount: ₹{amount:.2f}")





    