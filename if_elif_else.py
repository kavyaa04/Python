age=int(input("Enter age: "))

if age<18:
    print(f"Age {age} is not eligible for License")
elif age == 0:
    print("NA")
else:
    print(f"Age {age} is Eligible for License")
