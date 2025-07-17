firstNumber= int(input("Enter number ")) 
secondNumber = int(input("Enter number "))
thirdNumber = int(input("Enter number "))
sum = firstNumber + secondNumber + thirdNumber
average = sum / 3
product = firstNumber * secondNumber * thirdNumber
largest = 0
smallest = 0

if firstNumber > secondNumber and firstNumber > thirdNumber:
	largest = firstNumber
	print("The largest is ", largest)
if firstNumber < secondNumber and firstNumber < thirdNumber:
	smallest = firstNumber
	print("The smallest is ", smallest) 
if secondNumber > firstNumber and secondNumber > thirdNumber:
	largest = secondNumber
	print("The largest is ", largest)
if secondNumber < firstNumber and secondNumber < thirdNumber:
	smallest = secondNumber
	print("The smallest is ", smallest) 
if thirdNumber > firstNumber and thirdNumber > secondNumber:
	largest = thirdNumber
	print("The largest is ", largest)
if thirdNumber < secondNumber and thirdNumber < firstNumber:
	smallest = thirdNumber
	print("The smallest is ", smallest) 

print("The total of all numbers is ", sum , "and the average is", average, "and the product is", product)