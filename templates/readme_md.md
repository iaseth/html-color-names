
# html-color-names
HTML has [148 named colors](https://github.com/iaseth/html-color-names/blob/master/colors.json). What if you could generate a color palette using each one of them?




## How to use it with Tailwind

Install the [`html-color-names`](https://www.npmjs.com/package/html-color-names) npm package:
```
npm install --save-dev html-color-names
```

Import and add the colors to your `tailwind.config.js`
```javascript
const hcn = require("html-color-names");
const { htmlcolors } = hcn;
const { firebrick } = htmlcolors; // destructure all the HTML colors you want to use

export default {
	content: [],
	theme: {
		extend: {
			colors: {
				firebrick, // HTML color
			},
		},
	},
	plugins: [],
}
```

Now you can use the following classes in you HTML:

{{ firebrick.get_classes_from_css_as_table() }}




## Importing all colors

You can import all 148 colors into your Tailwind project by putting this in your `tailwind.config.js`
```javascript
const tailwindcolors = require('tailwindcss/colors');
const { slate, blue, white } = tailwindcolors; // destructure all the tailwind colors you want to use

const hcn = require("html-color-names");
const { htmlcolors } = hcn;

export default {
	content: [],
	theme: {
		colors: {
			...htmlcolors, // import all 148 color palettes
			slate, blue, white, // import all Tailwind colors, will overwrite colors if names clash
		},
		extend: {},
	},
	plugins: [],
}
```
Note that colors like`red`, `blue` and `orange` are present in both `htmlcolors` and `tailwindcolors`, so whichever you put last will overwrite the other. I recommend putting `tailwindcolors` last because its colors are handpicked and should be preferred over `htmlcolors` which is auto-generated.




## How I generate palettes?
I am using `python` to automatically generate palettes for each color. The basic logic for generating a palette is as follows:

* Each HTML color is assumed to be the `basecolor` and gets 5 `tints` and 5 `shades` to generate the palette.
* `tints` are colors between the `basecolor` and `White`.
* `shades` are colors between the `basecolor` and `Black`.
* `basecolor` is set to be `500`.
* `tints` are named from `50`, `100`, `200`, `300` and `400`.
* `shades` are named from `600`, `700`, `800`, `900` and `950`.
* The higher the `number`, the darker the color.




## Limitations
Since the palettes are automatically generated, there is no guarantee that the generated colors will look good. Some of the known problems you should watch out for, are:

* Saturated colors like `Red`, `Blue` and `Green` don't always look very good.
* Too light colors like `LightCyan` and `LightGoldenRodYellow` have too similar `tints` because there isn't enough gap between the color and `White`.
* Too dark colors like `DarkGreen` and `DarkBlue` have too similar `shades` because there isn't enough gap between the color and `Black`.




## List of HTML color palettes

| # | Name | className | Hex | CSS | JSON |
| --- | --- | --- | --- | --- | --- |{% for color in colors %}
| {{ loop.index }} | **{{ color.name }}** ![{{ color.name }}]({{ color.pngGithubRaw }}) | `{{ color.lowername }}` | `{{ color.hex }}` | [CSS]({{ color.cssGithub }}) | [JSON]({{ color.jsonGithub }}) |{% endfor %}


