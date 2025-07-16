principal = float(input("Enter principal amount: "))
yearlyRate = float(input("Enter yearly rate: "))
duration = float(input("Enter the duration in years"))
monthlyInterest = (yearlyRate / 100) / 12
monthsNumber = duration * 12





monthMortgage = monthlyInterest * ((1 + monthlyInterest) ** monthsNumber)
monthlyMortgage = ((1 + monthlyInterest) ** monthsNumber) - 1
months = monthMortgage / monthlyMortgage
result = principal * months

print(result)