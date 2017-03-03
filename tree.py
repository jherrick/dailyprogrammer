def tree(width, trunk, leaf):
	currentWidth = 1
	while currentWidth <= width:
		spacing = int(width/2 - currentWidth/2)

		print((' ' * spacing) + (leaf * currentWidth))

		currentWidth += 2

	spacing = int(width/2-1)

	print((' ' * spacing) + trunk *3)

tree(13, "=", "+")