import json
import os

import jinja2
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.abspath('./templates/')))

from pycolor import PyColor



def main():
	colorsJson = json.load(open("colors.json"))
	colors = [PyColor(c) for c in colorsJson["colors"]]
	[print(c) for c in colors]

	readme_md_template = jinja_env.get_template("readme_md.txt")
	readme_text = readme_md_template.render(
		colors=colors
	)

	with open("README.md", "w") as f:
		f.write(readme_text)
	print("saved: README.md")

if __name__ == '__main__':
	main()
