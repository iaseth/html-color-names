


def get_rgb_from_hex(hex):
	rgb = [0, 0, 0]
	rgb[0] = int(hex[1:3], 16)
	rgb[1] = int(hex[3:5], 16)
	rgb[2] = int(hex[5:7], 16)
	return rgb


