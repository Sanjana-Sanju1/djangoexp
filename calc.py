a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
print("1.add 2.subtract 3.multiplication 4.division ")
n=int(input("Enter your choice: "))
if n==1:
    s=a+b
    print(s)
elif n==2:
    s=a-b
    print(s)
elif n==3:
    s=a*b
    print(s)
elif n==4:
    s=a/b
    print(s)
else:
    print("incorrect choice")

