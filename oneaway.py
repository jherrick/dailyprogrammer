def oneaway(str1, str2):
	#true if strings are equal
	if str1==str2:
		return True
	#false if length difference is >= 2
	if abs(len(str1)-len(str2)) > 1:
		return False

	allowed = 1

	#find the longer string
	string = str1
	string2 = str2
	if len(str1) < len(str2):
		string = str2
		string2 = str1

	#shorter string will be first to 0
	while len(string2) > 0 and allowed > -1:
		#case #1, first element of both strings are the same
		if string[0] == string2[0]:
			string = string[1:]
			string2 = string2[1:]
		#case #2, first element of equal length strings are not the same
		elif len(string) == len(string2) and string[0] != string2[0]:
			string = string[1:]
			string2 = string2[1:]
			allowed -= 1
		#case #3, first element of unequal length strings are not the same
		else:
			string = string[1:]
			allowed -= 1

	if allowed < 0:
		return False

	return True

###  TEST CASES  ###

print oneaway("ple", "pale")
print oneaway("pale", "pales")
print oneaway("pale", "bale")
print oneaway("pale", "bake")
print oneaway("pale", "leap")
print oneaway("plp", "pale")