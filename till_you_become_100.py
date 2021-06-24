#If you find any way to make this code more efiicient,please tell me this will help a lot.
print("Select Mode: A} Normal  B) Advanced")
var = input()
varu = var.upper()

if varu == "A":
    name = input("What is your name? ")
    age = int(input("What is your age? "))

    while age <= 0:
        print(("Please enter a valid age :--"))
        age = int(input())

    age100 = 100 - age

    if not(age < 100):
        print("You are already 100!")
    else:
        print("You will be 100 in approximately",age100,"years!!")

else:
    name = input("What is your name? ")
    diff_year = int(input("Current Year: ")) - int(input("Birth Year: "))
    curnt_month = int(input("Current month: "))
    birth_month = int(input("Birth Month: "))
    diff_month = curnt_month - birth_month
    curnt_date = int(input("Current Date: "))
    birth_date = int(input("Birth Date: "))
    diff_date = curnt_date - birth_date
    if diff_month > 0:
        age = diff_year
    if diff_month == 0:
        if not(diff_date >= 0):
            age = diff_year
        else:
            age = diff_year-1
    if diff_month < 0:
        age = diff_year-1

    age100 = 100 - age

    if diff_month > 0:
        month_left = (12 - curnt_month) + birth_month
    if diff_month == 0:
        month_left = 0
    if diff_month < 0:
        month_left = birth_month - curnt_month

    if diff_date > 0:
        days_left = (30.5 - curnt_date) + birth_date
    if diff_date == 0:
        days_left = 0
    if diff_date < 0:
        days_left = birth_date - curnt_date

    while age <= 0:
        print(("Please enter a valid age :--"))
        age = int(input())

    if not(age < 100):
        print("You are already 100!")
    else:
        print(name, "you will be 100 years old in approxmately", age100,"years",month_left,"months",days_left,"days!!")
#If you find any way to make this code more efiicient,please tell me this will help a lot.
#also ignore the point in days, coz i took average