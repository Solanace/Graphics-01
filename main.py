def create(width, height):
	s = "P3\n" + str(width) + " " + str(height) + "\n255\n"
	for y in range(0, height):
		for x in range(0, height):
			s += str(x) + " " + str(y) + " " + str(x) + " "
		s += "\n"
	return s;

fd = open("image.ppm", "w")
fd.write(create(700, 700))
fd.close()