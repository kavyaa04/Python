#wap to find the currency of how mt i have to use to 500,100,20,10,5,2,1 to get 490

amt = 490

#500
n_500= amt//500
print(n_500)
amt= amt%500
print(f"amt balance: {amt}")

#100
n_100 =  amt//100
print(n_100)
amt = amt%100
print(f"amt balance: {amt}")

#20
n_20 = amt//20
print(n_20)
amt = amt%20
print(f"amt balance: {amt}")

##5
n_5 = amt//5
print(n_5)
amt = amt% 5
print(f"amt balance: {amt}")

##2
n_2 = amt//2
print(n_2)
amt = amt%2
print(f"amt balance: {amt}")

##1
n_1 = amt//1
print(n_1)
amt = amt%1
print(f"amt balance: {amt}")


print(f"500 * {n_500} + 100 * {n_100} + 20 * {n_20} + 5*{n_5} + 2*{n_2} + 1*{n_1} = {amt}")






