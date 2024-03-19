firstNum = int(input("Enter the first number = "))
secondNum = int(input("Enter the first number = "))
oper = input("Enter the Operater: ")

if oper == '+' :
    add = firstNum + secondNum
    print("Add the ", firstNum , "and", secondNum, "=", add)

elif oper == '-' :
    sub = firstNum - secondNum 
    print("Sub the ", firstNum , "and", secondNum, "=", sub)

elif oper == '*' :
    multi = firstNum - secondNum 
    print("multi the ", firstNum , "and", secondNum, "=", multi)

elif oper == '/' :
    divd = firstNum - secondNum 
    print("divd the ", firstNum , "and", secondNum, "=", divd)

elif oper == '%' :
    remb = firstNum - secondNum 
    print("remb the ", firstNum , "and", secondNum, "=", remb)

else :
    print("Wrong Entery")