import json
import math

from .utils import get_rgb_from_hex, get_hex_from_rgb



class PyColor:
	def __init__(self, rgb, name="Anoncolor"):
		self.rgb = rgb
		self.hex = get_hex_from_rgb(self.rgb)

		self.name = name
		self.lowername = self.name.lower()

		self.cssName = f"{self.lowername}.css"
		self.cssPath = f"css/{self.cssName}"
		self.cssGithub = f"https://github.com/iaseth/html-color-names/blob/master/{self.cssPath}"
		self.cssGithubRaw = f"https://raw.githubusercontent.com/iaseth/html-color-names/master/{self.cssPath}"

		self.jsonName = f"{self.lowername}.json"
		self.jsonPath = f"json/{self.jsonName}"
		self.jsonGithub = f"https://github.com/iaseth/html-color-names/blob/master/{self.jsonPath}"
		self.jsonGithubRaw = f"https://raw.githubusercontent.com/iaseth/html-color-names/master/{self.jsonPath}"

		self.pngName = f"{self.lowername}.png"
		self.pngPath = f"png/{self.pngName}"
		self.pngGithub = f"https://github.com/iaseth/html-color-names/blob/master/{self.pngPath}"
		self.pngGithubRaw = f"https://github.com/iaseth/html-color-names/blob/master/{self.pngPath}?raw=true"

		self.htmlName = f"{self.lowername}.html"
		self.htmlPath = f"docs/{self.htmlName}"
		self.docsPageURL = f"https://iaseth.github.io/html-color-names/{self.htmlName}"


	def as_object(self):
		jo = {}
		jo["name"] = self.name
		jo["lowername"] = self.lowername
		jo["hex"] = self.hex
		jo["rgb"] = self.rgb

		jo["cssName"] = self.cssName
		jo["cssPath"] = self.cssPath
		jo["cssGithub"] = self.cssGithub
		jo["cssGithubRaw"] = self.cssGithubRaw

		jo["jsonName"] = self.jsonName
		jo["jsonPath"] = self.jsonPath
		jo["jsonGithub"] = self.jsonGithub
		jo["jsonGithubRaw"] = self.jsonGithubRaw

		jo["pngName"] = self.pngName
		jo["pngPath"] = self.pngPath
		jo["pngGithub"] = self.pngGithub
		jo["pngGithubRaw"] = self.pngGithubRaw
		return jo

	def get_classes_from_css(self):
		text = open(self.cssPath).read()
		lines = text.split("\n")
		classes = [x.split("{")[0].strip() for x in lines if x.startswith(".")]
		return classes

	def get_classes_from_css_as_table(self):
		classes = self.get_classes_from_css()
		n = int(len(classes) / 4)
		text = "| Background | Text | Border | Outline |\n"
		text += "| --- | --- | --- | --- |\n"
		for x in range(n):
			k = x * 4
			text += f"| {classes[k]} | {classes[k+1]} | {classes[k+2]} | {classes[k+3]} |\n"
		return text


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

	def get_palette_json_text(self):
		jo = self.get_palette_json()
		text = json.dumps(jo, indent="\t")
		return text


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


