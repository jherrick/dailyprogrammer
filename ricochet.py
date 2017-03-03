def ricochet(h,w,v):
	height = h
	width = w
	location = [height, 0]
	while (height+width) not 0 and (height+width) not 7 and location not [0,w]:
		height -= 1
		width += 1
		if width = 3:
			while width != 0:
				width -= 1