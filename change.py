'''
def change(change):
	amount = change*100

	quarters = 0
	dimes = 0
	nickels = 0
	pennies = 0

	while amount > 0:
		while amount >= 25:
			quarters += 1
			amount -= 25
		while amount >= 10:
			dimes += 1
			amount -= 10
		while amount >= 5:
			nickels += 1
			amount -= 5
		while amount >= 1:
			pennies += 1
			amount -= 1

	if quarters > 0:
		print "Quarters: " + str(quarters)
	if dimes > 0:
		print "Dimes: " + str(dimes)
	if nickels > 0:
		print "Nickels: " + str(nickels)
	if pennies > 0:
		print "Pennies: " + str(pennies)

change(00.06)
'''

def change2(change):
	x = int( float(change) * 100)
	for i in [(25,"quarters"),(10,"dimes"),(5,"nickels"),(1,"pennies")]:
		x,y=(x%i[0],x//i[0])
		if y: print i[1] + ": " + str(y)

change2(1)


