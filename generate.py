import json
import os
import sys

from PIL import Image
import numpy
import jinja2
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('./templates/')))

from pycolor import get_color_from_json



def generate_readme(colors):
	readme_md_template = jinja_env.get_template("readme_md.md")
	readme_text = readme_md_template.render(
		colors=colors
	)

	with open("README.md", "w") as f:
		f.write(readme_text)
	print("saved: README.md")


def generate_css(colors):
	color_css_template = jinja_env.get_template("color_css.css")
	for color in colors:
		css_text = color_css_template.render(
			name=color.lowername,
			palette=color.get_palette()
		)

		with open(color.cssPath, "w") as f:
			f.write(css_text)
		print(f"saved: {color.cssPath}")


def generate_json(colors):
	for color in colors:
		with open(color.jsonPath, "w") as f:
			json.dump(color.get_palette_json(), f, indent="\t")
		print(f"saved: {color.jsonPath}")


def generate_html(colors):
	colorpage_html_template = jinja_env.get_template("colorpage.html")
	for color in colors:
		colorpage_text = colorpage_html_template.render(
			color=color
		)

		with open(color.htmlPath, "w") as f:
			f.write(colorpage_text)
		print(f"saved: {color.htmlPath}")

	homepage_html_template = jinja_env.get_template("homepage.html")
	homepage_html_text = homepage_html_template.render(
		colors=colors
	)

	homepage_path = "docs/index.html"
	with open(homepage_path, "w") as f:
		f.write(homepage_html_text)
	print(f"saved: {homepage_path}")


def generate_master_json(colors):
	jo = {}
	jo["colors"] = []
	for color in colors:
		colorJson = {}
		colorJson = color.as_object()
		colorJson["palette"] = color.get_palette_json()[color.lowername]
		jo["colors"].append(colorJson)

	master_json_path = "master.json"
	with open(master_json_path, "w") as f:
		json.dump(jo, f, indent="\t")
	print(f"saved: {master_json_path}")


def generate_master_css(colors):
	master_css_template = jinja_env.get_template("master_css.css")
	csspath = "master.css"
	css_text = master_css_template.render(
		colors=colors
	)

	with open(csspath, "w") as f:
		f.write(css_text)
	print(f"saved: {csspath}")


def generate_pngs(colors):
	SIZE = 50
	startY = 0
	endY = SIZE

	for color in colors:
		palette = color.get_palette()
		data = numpy.zeros((SIZE, SIZE*len(palette), 3), dtype=numpy.uint8)
		for idx, shade in enumerate(palette):
			startX = idx * SIZE
			endX = startX + SIZE
			for x in range(startX, endX):
				for y in range(startY, endY):
					data[y][x] = shade["rgb"]

		im = Image.fromarray(data)
		im.save(color.pngpath)
		print(f"saved: {color.pngpath}")


def main():
	colorsJson = json.load(open("colors.json"))
	colors = [get_color_from_json(jo) for jo in colorsJson["colors"]]

	args = sys.argv[1:]
	command = None if len(args) == 0 else args[0].lower()

	if command == "readme":
		generate_readme(colors)
	elif command == "css":
		generate_css(colors)
	elif command == "json":
		generate_json(colors)
	elif command == "html":
		generate_html(colors)
	elif command == "masterjson":
		generate_master_json(colors)
	elif command == "mastercss":
		generate_master_css(colors)
	elif command == "png":
		generate_pngs(colors)
	else:
		generate_readme(colors)


if __name__ == '__main__':
	main()
