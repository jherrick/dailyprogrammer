import json
import re

def mtgsearch():
	with open('AllCards.json') as file:
		json_obj = json.load(file)

	for i in json_obj:
		target = []
		player = []
		try:
			target = re.findall(r'target',json_obj[i]['text'])
			player = re.findall(r'player',json_obj[i]['text'])

			if len(target) >= 2 and "damage" in json_obj[i]['text'] and len(player) >= 2:
				print json_obj[i]['name']
				print json_obj[i]['text'].encode('utf-8')
				print "=================="
				print ""
		except KeyError:
			pass

mtgsearch()
