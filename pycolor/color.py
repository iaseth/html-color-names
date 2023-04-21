from .utils import get_rgb_from_hex, get_hex_from_rgb



class PyColor:
	def __init__(self, rgb, name="Anoncolor"):
		self.rgb = rgb
		self.name = name
		self.lowername = self.name.lower()
		self.hex = get_hex_from_rgb(self.rgb)

	def get_middle_colors(self, other, count):
		# returns 'n' colors between self and other
		pass

	def __str__(self):
		return f"PyColor '{self.name}' ({self.lowername}) {self.rgb}"


def get_color_from_json(jo):
	name = jo["name"]
	rgb = get_rgb_from_hex(jo["code"])
	color = PyColor(rgb, name)
	return color

def get_neutral(r):
	color = PyColor([r, r, r])
	return color


black = get_neutral(0)
grey = get_neutral(128)
white = get_neutral(255)


