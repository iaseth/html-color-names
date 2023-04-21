import math

from .utils import get_rgb_from_hex, get_hex_from_rgb



class PyColor:
	def __init__(self, rgb, name="Anoncolor"):
		self.rgb = rgb
		self.name = name
		self.lowername = self.name.lower()
		self.hex = get_hex_from_rgb(self.rgb)


	def get_middle_colors(self, other, count=5):
		# returns 'n' shades between self and other
		shades = []
		for x in range(count):
			components = []
			for c in range(3):
				gap = (other.rgb[c] - self.rgb[c])
				gap = math.floor(gap/(count+1))
				component = self.rgb[c] + (gap * (x+1))
				components.append(component)

			shade = PyColor(components)
			shades.append(shade)
		return shades

	def get_shades(self):
		return self.get_middle_colors(black)

	def get_tints(self):
		return self.get_middle_colors(white)

	def get_tones(self):
		return self.get_middle_colors(grey)

	def get_palette(self):
		palette = []
		tints = reversed(self.get_tints())
		palette += tints
		palette.append(self)

		shades = self.get_shades()
		palette += shades
		return palette


	def __str__(self):
		return f"PyColor '{self.name}' ({self.lowername}) {self.rgb}"

	def __repr__(self):
		return f"{self}"


def get_color_from_json(jo):
	name = jo["name"]
	rgb = get_rgb_from_hex(jo["code"])
	color = PyColor(rgb, name)
	return color

def get_neutral(r, name="Neutral"):
	color = PyColor([r, r, r], name)
	return color


black = get_neutral(0, "black")
grey = get_neutral(128, "grey")
white = get_neutral(255, "white")


