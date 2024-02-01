print("CALCULATOR")
a=int(input("enter first no:"))
b=int(input("enter second number"))
print("CALCULATOR\n 1.add\n 2.subtracrt\n 3.product\n 4.division")
n=int(input("enter the choice:"))
if n==1:
   c=a+b
   print(c)
elif n==2:
   c=a-b
   print(c)
elif n==3:
   c=a*b
   print(c)
elif n==4:
   c=a/b
   print(c)
else:
   print("INVALID CHOICE")
