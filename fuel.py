gauge = input("Enter a fraction: ")
x, y = gauge.split("/")

x = int(x)
y = int(y)

result = x / y
percentage = round(result * 100)


if percentage <= 1:
    print("Error")
elif percentage >= 99:
    print("Full")
else:
    print(f"{percentage}%")