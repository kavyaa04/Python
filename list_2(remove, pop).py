lists = [1,2,3,4,4,8,99,22,99]
val_remove = 99
if lists.count(val_remove)>0:
    lists.remove(val_remove)
    print(lists)
else:
    print("value not there")

print()
print("********************************")
print()

while val_remove in lists:
    lists.remove(val_remove)
print(lists)

print()
print("********************************")
print()

# l1 =[1,2,3,4]
# l1.remove(99)
# print(l1)              # Gives error as the valuse is not in the list (value error)  SO,

l1 =[1,2,3,4]

try:
    l1.remove(99)
    print("value removed")
except ValueError:
    print("value does not exist")



print()
print("***************POP()*****************")
print()



l= [1,2,3,4,5]
l.pop()
print(l)   #removes last element

vall = len(l)
print("lala: ", vall)

l.pop(3)
print(l)

print("length is: ",len(l))


print()
print("********************************")
print()

u = [1,2,3,4,5,6,7,7,8,9]
idx_to_remove = int(input("enter no:"))
if idx_to_remove< len(u) and idx_to_remove>= -len(u) :
    u.pop(idx_to_remove)
    
    print(u)
else:
    print("Index out of range")
