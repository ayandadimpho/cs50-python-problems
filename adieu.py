import sys

def main():
    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)
    except EOFError:
        print()


    message = "Adieu, addieu, to"

    if len(names) == 1:
        message += names[0]
    elif len(names) == 2:
        message += f"{names[0]} and {names[1]}"
    else:
        message += ", ".join(names)[:-1]
        message += f", and {names[-1]}"
    print(message)

if __name__ == "__main__":
    main()
