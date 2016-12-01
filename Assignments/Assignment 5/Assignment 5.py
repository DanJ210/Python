principal = int(input("Principal amount: "))
rate = float(input("Rate of interest: "))
compoundFrequency = int(input("Number of times per year to compound (12 if once per month): "))
years = float(input("Number of years for your investment: "))

amount = float(principal * (1 + rate / compoundFrequency) ** (compoundFrequency * years))

print("$" + "{0:.2f}".format(amount))
