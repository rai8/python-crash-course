num1=float(input("Enter the first number: "))
operator=input("Enter operator: ")
num2=float(input("Enter the second number: "))

if operator=="+":
    print (num1+num2)
elif operator == "-":
    print (num1-num2)
elif operator == "*":
     print (num1*num2)
elif operator == "/":
     print (num1/num2)
else:
    print("Sorry !!! This is an invalid operator")