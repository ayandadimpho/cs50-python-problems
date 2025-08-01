camel_case = input("camelcase variable: ")
snake_case = ""

for char in camel_case :
    if char.isupper() :
        snake_case += "_" + char.lower()
    else:
        snake_case += char
print(snake_case)