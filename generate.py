import json

from pycolor import PyColor



def main():
	colorsJson = json.load(open("colors.json"))
	colors = [PyColor(c) for c in colorsJson["colors"]]
	[print(c) for c in colors]

if __name__ == '__main__':
	main()
