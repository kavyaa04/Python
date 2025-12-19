import time
start = time.time()
n=9999999
#method -1
for i in range(n):
    avg = 18
    #method-1
    if avg>=80:
        print("a")
    elif avg>=60:
        print("b")
    elif avg>=40:
        print("c")
    elif avg>=20:
        print("d")
    else:
        pass
end1 = time.time()
print("Method 1 time taken", end1-start)


start= time.time()

#method-2
for i in range(n):
    avg = 18
    
    if avg>=80:
        print("a")
    if avg>=60 and avg<80:
        print("b")
    if avg>=40 and avg<60:
        print("c")
    if avg>=20 and avg<40:
        print("d")
    else:
        pass
end2  = time.time()

print("Method 2 time taken", end2-start)





n=5
for i in range(n+1):
    print("*")



