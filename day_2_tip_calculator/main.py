cost = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? "))
split = float(input("How many people to split the bill? "))

print(
    f"Each person should pay: {round((cost + (cost * (percentage / 100))) / split, 2)}"
)
