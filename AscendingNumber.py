firstNumber = float(input("Enter number: "))
secondNumber = float(input("Enter number: "))
thirdNumber = float(input("Enter number: "))

if firstNumber < secondNumber and firstNumber < thirdNumber and secondNumber > thirdNumber:
	print(firstNumber, thirdNumber, secondNumber)
if firstNumber < secondNumber and firstNumber < thirdNumber and thirdNumber > secondNumber:
	print(firstNumber, secondNumber, thirdNumber)
if secondNumber < firstNumber and secondNumber < thirdNumber and firstNumber > thirdNumber:
	print(secondNumber, thirdNumber, firstNumber)
if secondNumber < firstNumber and secondNumber < thirdNumber and thirdNumber > firstNumber:
	print(secondNumber, firstNumber, thirdNumber)
if thirdNumber < firstNumber and thirdNumber < secondNumber and firstNumber > secondNumber:
	print(thirdNumber, secondNumber, firstNumber)
if thirdNumber < firstNumber and thirdNumber < secondNumber and secondNumber > firstNumber:
	print(thirdNumber, firstnumberNumber, secondNumber)