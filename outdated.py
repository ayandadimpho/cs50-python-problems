def main():
    months = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()
        try:
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)


            elif "," in date:
                month_name, rest = date.split(" ", 1)
                day, year = rest.split(",")
                month = months.index(month_name.strip()) + 1
                day = int(day.strip())
                year = int(year.strip())


            else:
                continue
                
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
            break
        except (ValueError, IndexError):
            continue

main()

