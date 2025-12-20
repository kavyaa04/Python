n =5
for i in range(n):
   if i==0 or i==n-1 or i==n//2:
     print("* " * (n//2+1))
   else:
      print("*", " "*(n//2+1),"*")