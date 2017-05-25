'''
This challenge is to build a tourist booking engine where customers can book tours and 
activities around the Sydney. Specially, youre task today is to build the shopping cart system. 

These promotional rules have to be as flexible as possible as they will change in the future. 
Items can be added in any order.

https://www.reddit.com/r/dailyprogrammer/comments/6d29om/20170524_challenge_316_intermediate_sydney/
'''

class sydneyTours():
	def __init__(self):
		self.OH = 300
		self.BC = 110
		self.SK = 30
		self.tours = []

	def add(self, tour):
		self.tours.append(tour.split(' '))

	def promotionalRules(self, tour):
		discount = 0
		count = 0
		temp = {
				"OH": 0,
				"BC": 0,
				"SK": 0
			   }

		for item in tour:
			temp[item] += 1


		#place all promo deals below
			#3 for 2 OH opera house deal
			if item == "OH":
				count +=1
				if count == 3:
					discount += 300
					count = 0

		#bridge climb bulk discount
		if temp["BC"] > 4:
			discount += temp["BC"]*20

		#free SK with BC purchase
		if temp["SK"]>0 and temp["OH"]>0:
			if temp["BC"] > temp["SK"]:
				discount += temp["SK"]*self.SK
			else:
				discount += temp["OH"]*self.SK

		return discount, temp

	def total(self):
		print "Tour: " + "                 " + "Total: " 
		for tour in self.tours:
			discount, temp = self.promotionalRules(tour)
			total = temp["OH"]*self.OH + temp["SK"]*self.SK + temp["BC"]*self.BC - discount

			print str(tour) + " = " + "$" + str(total)

test = sydneyTours()

tour1 = "OH OH OH BC"
tour2 = "OH SK"
tour3 = "BC BC BC BC BC OH"

test.add(tour1)
test.add(tour2)
test.add(tour3)
test.total()