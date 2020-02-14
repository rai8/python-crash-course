def max_num(num1,num2,num3):
    if num1>=num2 and num1>num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    elif num3>=num1 and num3>=num2:
        return num3
    else:
        return ("They are both equal")

print (max_num(67,5,45))
print (max_num(45,45,45))