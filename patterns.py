'''def patterns(pattern):
	file = open("enable1.txt", "r")
	words = file.readlines()

	checker = pattern

	letters = {
			  "X": "",
			  "Y": "",
			  "Z": "",
			  }

	answer = []

	for word in words:
		if len(word)>=len(pattern):
			letters[checker[1]] = word[1]
			while letters[checker[1]] == word[1]:
				word = word[1:]
				checker = checker[1:]
				if len(checker) == 0:
					answer.append(word)
					checker = pattern
					break
				if letters[checker[1]] == "":
					letters[checker[1]] = word[1]
				
	return answer

print patterns("XXYYZZ")'''

# regex solution below #

"""
Find all words that contain the submitted pattern using the format builtin.
Requires enable1.txt word file.
"""

pat = input('Please enter a search pattern:')
pat_length = len(pat)

# Create mapping of pattern chars to positionals for use in .format
dict = {}
for i in range(0, pat_length):
    #Only one entry in dict per unique char
    if pat[i] not in dict:
        dict[pat[i]] = str(i)

# Convert pattern to usable format string
srch_str = ''
for c in pat:
    srch_str += '{' + dict[c] + '}'
print dict
print pat
print srch_str

with open('enable1.txt', 'r') as f:
    for word in f:
        word = word.strip('\n')
        for i in range(0, len(word) - pat_length + 1):
            word_slice = word[i:i + pat_length]
            if srch_str.format(*word_slice) == word[i:i + pat_length]:
                print(word)







