num=85
attempt =0
lives =2

while True:
    guess = int(input("enter num: "))
        
    attempt+=1

    if guess==num:
        print("yayyy u did it")
        print(f"The number of attempts is {attempt}")
        break
    else:
        print("wrong")
        lives-=1
        print(" The no of lives left is ", lives)
        if lives==0:
            print("Game over")
            break
        

    
