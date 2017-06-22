import re 

def condense(sentence):
    print re.sub('(\S+)\s+\\1','\\1',sentence)

if __name__ == '__main__':
	examples = ["I heard the pastor sing live verses easily.",
			   "Deep episodes of Deep Space Nine came on the television only after the news.",
			   "Digital alarm clocks scare area children."]

	for example in examples:
		condense(example)