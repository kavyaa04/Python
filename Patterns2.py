''' 
* _ _ _ _ *
* _ _ _ _ *
* _ _ _ _ *
* _ _ _ _ *
* _ _ _ _ *
'''

n=5
for i in range(n):
    for j in  range(n):
        if(j==0 or j== n-1 or i==j or i+j==n-1  ):
            print("*", end=" ")
        else:
            print(' ',end=" ")
    print()

print()
print("----------*****----------")
print()


n=5
for i in range(n):
    for j in range(n):
        if(i==n//2 or j==n//2):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


print()
print("----------*****----------")
print()

n=5
for i in range(n):
    for j in range(n):
        if(i==j or i+j==n-1):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


print()
print("----------*****----------")
print()


n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==n-1 or j==0 or j==n-1):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()


print()
print("----------*****----------")
print()


n=5
for i in range(n):
    for j in range(i+1):
        if(j==0 or i==n-1 or i==j):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
        
   


print()
print("----------*****----------")
print()



n=5
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
        
   
print()
print("----------*****----------")
print()


n=5
for i in range(n):
    for j in range(n):
        if i+j<=n-1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()
        
   
print()
print("----------*****----------")
print()




n=5
for i in range(n):
    for j in range(n):
        if (j==0 and i==0):
            print("*", end=" ")
        elif(i==1):
            print(" ",end=" ")
    print()
        
   
print()
print("----------*****----------")
print()