sum_gallons = 0
sum_miles = 0
while(True):
	gallons_used = float(input('Enter the gallons used(-1 to end)'))
	if gallons_used == -1:
		print(sum_miles / sum_gallons) 
		break
	miles_driven = float(input('Enter the miles driven'))
	calculate = miles_driven / gallons_used
	print(calculate);
	sum_gallons += gallons_used
	sum_miles += miles_driven
