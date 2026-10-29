print("===================================")
print("     CALENDAR VERIFICATION SYSTEM")
print("===================================")

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Enter a positive year.")

else:
    print("\n-----------------------------------")
    print("Year:", year)

    if year % 100 == 0:
        if year % 400 == 0:
            print("Status: LEAP YEAR")
            print("Reason: Century year divisible by 400")
            days = 366
            feb_days = 29
        else:
            print("Status: COMMON YEAR")
            print("Reason: Century year not divisible by 400")
            days = 365
            feb_days = 28

    elif year % 4 == 0:
        print("Status: LEAP YEAR")
        print("Reason: Divisible by 4 and not a century year")
        days = 366
        feb_days = 29

    else:
        print("Status: COMMON YEAR")
        print("Reason: Not divisible by 4")
        days = 365
        feb_days = 28

    print("Days in Year:", days, "days")
    print("Days in February:", feb_days, "days")
    print("-----------------------------------")