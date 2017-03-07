### 3/7/17 daily challenge -- permutation base ###
### https://www.reddit.com/r/dailyprogrammer/comments/5xu7sz/20170306_challenge_305_easy_permutation_base/ ###

def permbase2_inv(number):
	return int(number, base=2) + 2**(len(number))-2

def permbase2(number):
	n = 1
	while(2**n <= number):
		number -= 2**n
		n += 1
	return '{0:0{count}b}'.format(number, count = n)

print permbase2_inv("1")

print permbase2(1)


