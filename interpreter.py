expression = input("Give an arithmetic expression ")
x,y,z = expression.split()

x = int(x)
z = int(z)


if y == "+":
    result = round(x + z, 1)
    print(result)
elif y == "/":
    result = round(x / z, 1)
    print(result)
elif y == "*":
    result = round(x * z, 1)
    print(result)
elif y == "-":
    result = round(x - z, 1)
    print(result)
else:
    print ("Error:Invalid Operator")