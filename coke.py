amount_due = 50 
coins_inserted = 0


while coins_inserted < amount_due :
    money = int(input("Insert your coin (5, 10, or 25): "))


    if money == 5 or money == 10 or money == 25 :
        coins_inserted += money
    else:
        print("Unrecognized coin")
    if coins_inserted < amount_due :
        print("Amount due: ", amount_due - coins_inserted)


print("Change owed:", coins_inserted - amount_due)

