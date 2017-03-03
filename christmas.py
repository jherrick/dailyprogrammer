def TwelveDays():
	days = ["first", 
			"second", 
			"third", 
			"fourth", 
			"fifth", 
			"sixth", 
			"seventh", 
			"eighth", 
			"ninth", 
			"tenth", 
			"eleventh", 
			"twelfth"]

	gifts = ["Partridge in a Pear Tree",
			 "Turtle Doves",
			 "French Hens",
			 "Calling Birds",
			 "Golden Rings",
			 "Geese a Laying",
			 "Swans a Swimming",
			 "Maids a Milking",
			 "Ladies Dancing",
			 "Lords a Leaping",
			 "Pipers Piping",
			 "Drummers Drumming"]

	i = 0

	for day in days:
		print "On the " + day + " day of Christmas"
		print "my true love sent to me:"
		j = i
		while j >= 0:
			if i > 0 and j == 0:
				print "and " + str(j+1) + " " + gifts[j]
			else:
				print str(j+1) + " " + gifts[j]
			j-=1
		print ""
		i += 1

TwelveDays()