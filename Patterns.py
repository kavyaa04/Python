n=5
k=1
for i in range(n):
    for j in range(k):
        print("*", end=" ")
    k+=1
    print()

print("----------*****----------")
print()
#WITH SAME VARIABLES

n=5
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

print("----------*****----------")
print()

n=int(input("enter no: "))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()

print("----------*****----------")
print()

n=int(input("enter no: "))
for i in range(n):
    print(n)
