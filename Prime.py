num = int(input("enter num: "))

if(num<=1):
    print("not prime")
else:
    isPrime = True
    for i in range(2,num):
        if num % 1 ==0:
            isPrime = False
            break
    
if (isPrime== True):
    print("prime")
else:
    print("no")



#Prime Nos in list

low, high = 2, 10
primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)

print(primes)
