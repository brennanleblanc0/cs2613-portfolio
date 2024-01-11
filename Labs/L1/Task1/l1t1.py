name = input("Hello! Please input a name:\n")
goodAge = False
age : int
age = int(input("Please input an age:\n"))
while not goodAge:
    if age >= 0 and age <= 122:
        goodAge = True
    else:
        age = int(input("Error with age, please input a new age:\n"))

if age >= 0 and age <= 15:
    print(f"{name} must wait {16-age} more years to get a driver's license!")
elif age == 16:
    print(f"Congrats! {name} can get their driver's license now!")
else:
    print(f"{name} has been eligible for a driver's license for {age-16} years!")