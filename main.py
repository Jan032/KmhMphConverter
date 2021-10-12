print("Hi! i'm a programme that converts Kilometers into Miles")

km = int(input("Input Kilometers: "))
print(km * 0.6213)

a = input("do you want to do another conversion?: ")
while a == "yes" or a == "Yes" or a == "YES":
    km = int(input("input kilometers: "))
    miles = (km * 0.6213)
    print(miles)
    a = input("do you want to do another conversion?: ")
    if a == "no" or a == "No" or a == "NO":
        break
print("goodbye!")
