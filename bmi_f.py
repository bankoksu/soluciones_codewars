def bmi(weight, height):
	imc = weight / height ** 2

	if imc <= 18,5:
		print "Underweight"

	elif imc <= 25,0:
		print "Normal"

	elif imc <= 30,0:
		print "Overweight"

	elif imc > 30:
		print "Obese"

	



print (bmi(50, 1.80)
print (bmi(80, 1.80)
print (bmi(90, 1.80)
print (bmi(110, 1.80)
print (bmi(50, 1.50)
