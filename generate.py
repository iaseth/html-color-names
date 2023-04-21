import json
import os
import sys

import jinja2
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('./templates/')))

from pycolor import get_color_from_json



def generate_readme(colors):
	readme_md_template = jinja_env.get_template("readme_md.txt")
	readme_text = readme_md_template.render(
		colors=colors
	)

	with open("README.md", "w") as f:
		f.write(readme_text)
	print("saved: README.md")


def generate_css(colors):
	color_css_template = jinja_env.get_template("color_css.txt")
	for color in colors:
		csspath = color.csspath
		css_text = color_css_template.render(
			name=color.lowername,
			palette=color.get_palette()
		)

		with open(csspath, "w") as f:
			f.write(css_text)
		print(f"saved: {csspath}")


def generate_json(colors):
	for color in colors:
		with open(color.jsonpath, "w") as f:
			json.dump(color.get_palette_json(), f, indent="\t")
		print(f"saved: {color.jsonpath}")


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
	else:
		generate_readme(colors)


if __name__ == '__main__':
	main()
