
# html-color-names
HTML has 148 named colors. What if you could generate a color palette using each of them?

## How to use it with Tailwind

Install the [`html-color-names`](https://www.npmjs.com/package/html-color-names) npm package:
```
npm install html-color-names
```

Import and add the colors to your `tailwind.config.js`
```javascript
const tailwindcolors = require('tailwindcss/colors');
const {slate} = tailwindcolors; // destructure all the tailwind colors you want to use

const hcn = require("html-color-names");
const {htmlcolors} = hcn;
const {firebrick} = htmlcolors; // destructure all the HTML colors you want to use

export default {
	content: [],
	theme: {
		colors: {
			firebrick, // HTML color
			slate, // Tailwind color
		},
		extend: {},
	},
	plugins: [],
}
```

| # | Name | className | Hex | CSS | JSON |
| --- | --- | --- | --- | --- | --- |{% for color in colors %}
| {{ loop.index }} | **{{ color.name }}** ![{{ color.name }}]({{ color.png_github_raw }}) | `{{ color.lowername }}` | `{{ color.hex }}` | [CSS]({{ color.css_github }}) | [JSON]({{ color.json_github }}) |{% endfor %}


