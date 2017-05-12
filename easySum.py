'''
Given a sorted list of distinct integers, write a function that returns whether 
there are two integers in the list that add up to 0. For example, you would 
return true if both -14435 and 14435 are in the list, because -14435 + 14435 = 0. 
Also return true if 0 appears in the list. '''

def subSum(data):
	check = [abs(num) for num in data]

	if len(check) != len(set(check)) or 0 in check:
		return True 

	return False 

def main():
	tests = [[1,2,3],[-5,-3,-1,2,4,6],[],[-97364, -71561, -69336, 19675, 71561, 97863], [-53974, -39140, -36561, -23935, -15680, 0]]
	for test in tests:
		print subSum(test)

if __name__ == "__main__":
	main()
