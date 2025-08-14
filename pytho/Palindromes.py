number = 12121
number_one = str(number % 10)
number_two = str((number // 10) % 10)
number_three = str((number // 100) % 10)
number_four = str((number // 1000) % 10)
number_five = str((number // 1000) // 10)
result = ""
numbers = str(number)
result = number_one + number_two + number_three + number_four + number_five
print(result)
if result == numbers:
	print('It is a palindrome')
else:
	print('It is not a palindrome')