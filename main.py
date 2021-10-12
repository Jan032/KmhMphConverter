
print("Hi! i'm a programme that converts Kilometers into Miles")

km = int(input("Input Kilometers: "))
print(km * 0.6213)

a = (input("do you want to do another conversion?: "))
a = a.lower()

while a == "yes":
    km = int(input("input kilometers: "))
    miles = (km * 0.6213)
    print(miles)
    a = (input("do you want to do another conversion?: "))
    if a == "no":
        break

print("goodbye!")
