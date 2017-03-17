def main(choice, text):
	listed = text.split()

	if choice == 0:
		listed = [listed[0]] + [s.capitalize() for s in listed[1:]]
		print ''.join(listed)

	elif choice == 1:
		print '_'.join(listed)

	elif choice == 2:
		print '_'.join([word.upper() for word in listed])

if __name__ == '__main__':
	main(2, "hello world")