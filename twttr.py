message = input("Enter your tweet: ")
vowels = "aeiouAEIOU"

output = ""
for char in message :
    if char not in vowels:
        output += char

print(output)