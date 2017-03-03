'''
def parsing(notation):

	separators = ["-", ":", ".", ","]

	cleaned = []

	temp = ""

	for x in notation:
		if x not in separators:
			temp += x
		else:
			cleaned.append(temp)
			temp = ""
			if x is not ",":
				cleaned.append(x)
	cleaned.append(temp)

	answer = []

	answer.append(cleaned[0])

	print cleaned

	for x in range(1, len(cleaned)):

		counter = pow(10, len(cleaned[x]))
		if cleaned[x] not in separators:
			if int(cleaned[x]) < int(answer[-1]):
				while (int(cleaned[x])+counter) < int(answer[-1]):
					counter += pow(10, len(cleaned[x]))
				answer.append(int(cleaned[x])+counter)
			else:
				answer.append(cleaned[x])

		if cleaned[x] == "-" or cleaned[x] == ":":
			counter = pow(10, len(cleaned[x+1]))
			while int(cleaned[x-1]) > int(cleaned[x+1])+counter:
					counter = pow(10, len(cleaned[x+1]))
			for y in range((int(cleaned[x+1])+counter-1)-int(cleaned[x-1])):
				answer.append(int(cleaned[x-1])+y)

		#if cleaned[x] == ":":


	for x in answer:
		print x,

parsing("545,64:11")

'''
# ---------- SOLUTION --------------- #

def main(inp):
    out = [0]
    for range_str in inp.strip().split(','):
        range_nums = split_range(range_str, ['-', ':', '..'])
        start_num = find_next_largest(out[-1], range_nums[0])
        if len(range_nums) == 1:
            out.append(start_num)
        else:
            end_num = find_next_largest(start_num, range_nums[1]) + 1
            new_range_nums = [int(n) for n in range_nums]
            new_range_nums[0:2] = [start_num, end_num]
            out.extend(range(*new_range_nums))
    print(' '.join(str(n) for n in out[1:]), '\n')

def find_next_largest(current_largest, n):
    new_largest = int(n)
    while new_largest < current_largest:
        new_largest += pow(10, len(n))
    return new_largest

def split_range(range_str, seperators):
    for sep in seperators:
        if sep in range_str:
            return range_str.split(sep)
    return [range_str]


if __name__ == '__main__':
    inps = ["1,3,7,2,4,1", "1-3,1-2", "1:5:2", "104-2", "104..02", "545,64:11"]
    for inp in inps:
        main(inp)



