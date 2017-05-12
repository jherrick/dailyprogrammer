def oneaway2(str1, str2):
	if str1==str2:
		return True
	if abs(len(str1)-len(str2)) > 1:
		return False

	allowed = 1

	y = 0

	for char in range(min(len(str1), len(str2))):
		if len(str1) != len(str2) and str1[char] != str2[y]:
			allowed -= 1
			if allowed < 0:
				return False
		elif str1[char] != str2[y]:
			allowed -= 1
			if allowed < 0:
				return False
			y += 1
		else:
			y += 1
	return True

print oneaway("pale", "ple")
print oneaway("pales", "pale")
print oneaway("pale", "bale")
print oneaway("pale", "bake")
print oneaway("pale", "leap")
print oneaway("pale", "plp")