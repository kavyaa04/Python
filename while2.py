# num1 =85
# guess = int(input("enter the number: "))
# if guess == num1:
#     print("congrats!!")
# else:
#     print("sorryy!!")

# print()
print("*************-------------************")

num2 = 85
attempt=0

while True:
    guess = int(input("enter the number: "))
    attempt+=1

    if guess == num2:
        print("yayyy!!")

    else:
        print("sorry2")
    print(f"The attempt is {attempt}")
