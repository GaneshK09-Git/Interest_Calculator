#Python compound interest calculator


principle = 0
rate_of_interest = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break

while True:
    rate_of_interest = float(input("Enter the interest rate: "))
    if rate_of_interest < 0:
        print("interest rate can't be less than zero")
    else:
        break

while True:
    time = float(input("Enter the time: "))
    if time < 0:
        print("time can't be be less than zero")
    else:
        break

total = principle * pow((1+ rate_of_interest/100),time)
print(f"Balance after {time} year/s: ${total:.2f}")