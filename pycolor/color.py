import math

from .utils import get_rgb_from_hex, get_hex_from_rgb



class PyColor:
	def __init__(self, rgb, name="Anoncolor"):
		self.rgb = rgb
		self.hex = get_hex_from_rgb(self.rgb)

		self.name = name
		self.lowername = self.name.lower()

		self.cssname = f"{self.lowername}.css"
		self.csspath = f"css/{self.cssname}"
		self.css_github = f"https://github.com/iaseth/html-color-names/blob/master/css/{self.lowername}.css"
		self.css_github_raw = f"https://raw.githubusercontent.com/iaseth/html-color-names/master/css/{self.lowername}.css"

		self.jsonname = f"{self.lowername}.json"
		self.jsonpath = f"json/{self.jsonname}"
		self.json_github = f"https://github.com/iaseth/html-color-names/blob/master/json/{self.lowername}.json"
		self.json_github_raw = f"https://raw.githubusercontent.com/iaseth/html-color-names/master/json/{self.lowername}.json"



	def get_middle_colors(self, other, count=5):
		# returns 'n' shades between self and other
		shades = []
		for x in range(count):
			components = []
			for c in range(3):
				gap = other.rgb[c] - self.rgb[c]
				step = gap/(count+1)
				offset = step * (x+1)
				component = int(self.rgb[c] + offset)
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
		colors = []
		tints = reversed(self.get_tints())
		colors += tints
		colors.append(self)

		shades = self.get_shades()
		colors += shades

		values = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
		palette = []
		for idx, color in enumerate(colors):
			entry = {}
			entry["value"] = values[idx]
			entry["hex"] = color.hex
			entry["rgb"] = color.rgb
			palette.append(entry)
		return palette

	def get_palette_json(self):
		jo = {}
		jo[self.lowername] = {}
		palette = self.get_palette()
		for color in palette:
			jo[self.lowername][color["value"]] = color["hex"]
		return jo


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


