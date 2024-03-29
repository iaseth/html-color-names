
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

| Background | Text | Border | Outline |
| --- | --- | --- | --- |
| `.bg-firebrick-50` | `.text-firebrick-50` | `.border-firebrick-50` | `.outline-firebrick-50` |
| `.bg-firebrick-100` | `.text-firebrick-100` | `.border-firebrick-100` | `.outline-firebrick-100` |
| `.bg-firebrick-200` | `.text-firebrick-200` | `.border-firebrick-200` | `.outline-firebrick-200` |
| `.bg-firebrick-300` | `.text-firebrick-300` | `.border-firebrick-300` | `.outline-firebrick-300` |
| `.bg-firebrick-400` | `.text-firebrick-400` | `.border-firebrick-400` | `.outline-firebrick-400` |
| `.bg-firebrick-500` | `.text-firebrick-500` | `.border-firebrick-500` | `.outline-firebrick-500` |
| `.bg-firebrick-600` | `.text-firebrick-600` | `.border-firebrick-600` | `.outline-firebrick-600` |
| `.bg-firebrick-700` | `.text-firebrick-700` | `.border-firebrick-700` | `.outline-firebrick-700` |
| `.bg-firebrick-800` | `.text-firebrick-800` | `.border-firebrick-800` | `.outline-firebrick-800` |
| `.bg-firebrick-900` | `.text-firebrick-900` | `.border-firebrick-900` | `.outline-firebrick-900` |
| `.bg-firebrick-950` | `.text-firebrick-950` | `.border-firebrick-950` | `.outline-firebrick-950` |





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
| --- | --- | --- | --- | --- | --- |
| 1 | **AliceBlue** ![AliceBlue](https://github.com/iaseth/html-color-names/blob/master/png/aliceblue.png?raw=true) | `aliceblue` | `#f0f8ff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/aliceblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/aliceblue.json) |
| 2 | **AntiqueWhite** ![AntiqueWhite](https://github.com/iaseth/html-color-names/blob/master/png/antiquewhite.png?raw=true) | `antiquewhite` | `#faebd7` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/antiquewhite.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/antiquewhite.json) |
| 3 | **Aqua** ![Aqua](https://github.com/iaseth/html-color-names/blob/master/png/aqua.png?raw=true) | `aqua` | `#00ffff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/aqua.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/aqua.json) |
| 4 | **Aquamarine** ![Aquamarine](https://github.com/iaseth/html-color-names/blob/master/png/aquamarine.png?raw=true) | `aquamarine` | `#7fffd4` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/aquamarine.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/aquamarine.json) |
| 5 | **Azure** ![Azure](https://github.com/iaseth/html-color-names/blob/master/png/azure.png?raw=true) | `azure` | `#f0ffff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/azure.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/azure.json) |
| 6 | **Beige** ![Beige](https://github.com/iaseth/html-color-names/blob/master/png/beige.png?raw=true) | `beige` | `#f5f5dc` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/beige.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/beige.json) |
| 7 | **Bisque** ![Bisque](https://github.com/iaseth/html-color-names/blob/master/png/bisque.png?raw=true) | `bisque` | `#ffe4c4` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/bisque.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/bisque.json) |
| 8 | **Black** ![Black](https://github.com/iaseth/html-color-names/blob/master/png/black.png?raw=true) | `black` | `#000000` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/black.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/black.json) |
| 9 | **BlanchedAlmond** ![BlanchedAlmond](https://github.com/iaseth/html-color-names/blob/master/png/blanchedalmond.png?raw=true) | `blanchedalmond` | `#ffebcd` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/blanchedalmond.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/blanchedalmond.json) |
| 10 | **Blue** ![Blue](https://github.com/iaseth/html-color-names/blob/master/png/blue.png?raw=true) | `blue` | `#0000ff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/blue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/blue.json) |
| 11 | **BlueViolet** ![BlueViolet](https://github.com/iaseth/html-color-names/blob/master/png/blueviolet.png?raw=true) | `blueviolet` | `#8a2be2` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/blueviolet.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/blueviolet.json) |
| 12 | **Brown** ![Brown](https://github.com/iaseth/html-color-names/blob/master/png/brown.png?raw=true) | `brown` | `#a52a2a` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/brown.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/brown.json) |
| 13 | **BurlyWood** ![BurlyWood](https://github.com/iaseth/html-color-names/blob/master/png/burlywood.png?raw=true) | `burlywood` | `#deb887` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/burlywood.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/burlywood.json) |
| 14 | **CadetBlue** ![CadetBlue](https://github.com/iaseth/html-color-names/blob/master/png/cadetblue.png?raw=true) | `cadetblue` | `#5f9ea0` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/cadetblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/cadetblue.json) |
| 15 | **Chartreuse** ![Chartreuse](https://github.com/iaseth/html-color-names/blob/master/png/chartreuse.png?raw=true) | `chartreuse` | `#7fff00` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/chartreuse.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/chartreuse.json) |
| 16 | **Chocolate** ![Chocolate](https://github.com/iaseth/html-color-names/blob/master/png/chocolate.png?raw=true) | `chocolate` | `#d2691e` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/chocolate.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/chocolate.json) |
| 17 | **Coral** ![Coral](https://github.com/iaseth/html-color-names/blob/master/png/coral.png?raw=true) | `coral` | `#ff7f50` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/coral.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/coral.json) |
| 18 | **CornflowerBlue** ![CornflowerBlue](https://github.com/iaseth/html-color-names/blob/master/png/cornflowerblue.png?raw=true) | `cornflowerblue` | `#6495ed` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/cornflowerblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/cornflowerblue.json) |
| 19 | **Cornsilk** ![Cornsilk](https://github.com/iaseth/html-color-names/blob/master/png/cornsilk.png?raw=true) | `cornsilk` | `#fff8dc` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/cornsilk.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/cornsilk.json) |
| 20 | **Crimson** ![Crimson](https://github.com/iaseth/html-color-names/blob/master/png/crimson.png?raw=true) | `crimson` | `#dc143c` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/crimson.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/crimson.json) |
| 21 | **Cyan** ![Cyan](https://github.com/iaseth/html-color-names/blob/master/png/cyan.png?raw=true) | `cyan` | `#00ffff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/cyan.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/cyan.json) |
| 22 | **DarkBlue** ![DarkBlue](https://github.com/iaseth/html-color-names/blob/master/png/darkblue.png?raw=true) | `darkblue` | `#00008b` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkblue.json) |
| 23 | **DarkCyan** ![DarkCyan](https://github.com/iaseth/html-color-names/blob/master/png/darkcyan.png?raw=true) | `darkcyan` | `#008b8b` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkcyan.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkcyan.json) |
| 24 | **DarkGoldenRod** ![DarkGoldenRod](https://github.com/iaseth/html-color-names/blob/master/png/darkgoldenrod.png?raw=true) | `darkgoldenrod` | `#b8860b` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkgoldenrod.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkgoldenrod.json) |
| 25 | **DarkGray** ![DarkGray](https://github.com/iaseth/html-color-names/blob/master/png/darkgray.png?raw=true) | `darkgray` | `#a9a9a9` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkgray.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkgray.json) |
| 26 | **DarkGrey** ![DarkGrey](https://github.com/iaseth/html-color-names/blob/master/png/darkgrey.png?raw=true) | `darkgrey` | `#a9a9a9` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkgrey.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkgrey.json) |
| 27 | **DarkGreen** ![DarkGreen](https://github.com/iaseth/html-color-names/blob/master/png/darkgreen.png?raw=true) | `darkgreen` | `#006400` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkgreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkgreen.json) |
| 28 | **DarkKhaki** ![DarkKhaki](https://github.com/iaseth/html-color-names/blob/master/png/darkkhaki.png?raw=true) | `darkkhaki` | `#bdb76b` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkkhaki.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkkhaki.json) |
| 29 | **DarkMagenta** ![DarkMagenta](https://github.com/iaseth/html-color-names/blob/master/png/darkmagenta.png?raw=true) | `darkmagenta` | `#8b008b` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkmagenta.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkmagenta.json) |
| 30 | **DarkOliveGreen** ![DarkOliveGreen](https://github.com/iaseth/html-color-names/blob/master/png/darkolivegreen.png?raw=true) | `darkolivegreen` | `#556b2f` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkolivegreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkolivegreen.json) |
| 31 | **DarkOrange** ![DarkOrange](https://github.com/iaseth/html-color-names/blob/master/png/darkorange.png?raw=true) | `darkorange` | `#ff8c00` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkorange.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkorange.json) |
| 32 | **DarkOrchid** ![DarkOrchid](https://github.com/iaseth/html-color-names/blob/master/png/darkorchid.png?raw=true) | `darkorchid` | `#9932cc` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkorchid.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkorchid.json) |
| 33 | **DarkRed** ![DarkRed](https://github.com/iaseth/html-color-names/blob/master/png/darkred.png?raw=true) | `darkred` | `#8b0000` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkred.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkred.json) |
| 34 | **DarkSalmon** ![DarkSalmon](https://github.com/iaseth/html-color-names/blob/master/png/darksalmon.png?raw=true) | `darksalmon` | `#e9967a` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darksalmon.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darksalmon.json) |
| 35 | **DarkSeaGreen** ![DarkSeaGreen](https://github.com/iaseth/html-color-names/blob/master/png/darkseagreen.png?raw=true) | `darkseagreen` | `#8fbc8f` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkseagreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkseagreen.json) |
| 36 | **DarkSlateBlue** ![DarkSlateBlue](https://github.com/iaseth/html-color-names/blob/master/png/darkslateblue.png?raw=true) | `darkslateblue` | `#483d8b` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkslateblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkslateblue.json) |
| 37 | **DarkSlateGray** ![DarkSlateGray](https://github.com/iaseth/html-color-names/blob/master/png/darkslategray.png?raw=true) | `darkslategray` | `#2f4f4f` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkslategray.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkslategray.json) |
| 38 | **DarkSlateGrey** ![DarkSlateGrey](https://github.com/iaseth/html-color-names/blob/master/png/darkslategrey.png?raw=true) | `darkslategrey` | `#2f4f4f` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkslategrey.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkslategrey.json) |
| 39 | **DarkTurquoise** ![DarkTurquoise](https://github.com/iaseth/html-color-names/blob/master/png/darkturquoise.png?raw=true) | `darkturquoise` | `#00ced1` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkturquoise.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkturquoise.json) |
| 40 | **DarkViolet** ![DarkViolet](https://github.com/iaseth/html-color-names/blob/master/png/darkviolet.png?raw=true) | `darkviolet` | `#9400d3` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/darkviolet.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/darkviolet.json) |
| 41 | **DeepPink** ![DeepPink](https://github.com/iaseth/html-color-names/blob/master/png/deeppink.png?raw=true) | `deeppink` | `#ff1493` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/deeppink.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/deeppink.json) |
| 42 | **DeepSkyBlue** ![DeepSkyBlue](https://github.com/iaseth/html-color-names/blob/master/png/deepskyblue.png?raw=true) | `deepskyblue` | `#00bfff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/deepskyblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/deepskyblue.json) |
| 43 | **DimGray** ![DimGray](https://github.com/iaseth/html-color-names/blob/master/png/dimgray.png?raw=true) | `dimgray` | `#696969` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/dimgray.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/dimgray.json) |
| 44 | **DimGrey** ![DimGrey](https://github.com/iaseth/html-color-names/blob/master/png/dimgrey.png?raw=true) | `dimgrey` | `#696969` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/dimgrey.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/dimgrey.json) |
| 45 | **DodgerBlue** ![DodgerBlue](https://github.com/iaseth/html-color-names/blob/master/png/dodgerblue.png?raw=true) | `dodgerblue` | `#1e90ff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/dodgerblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/dodgerblue.json) |
| 46 | **FireBrick** ![FireBrick](https://github.com/iaseth/html-color-names/blob/master/png/firebrick.png?raw=true) | `firebrick` | `#b22222` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/firebrick.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/firebrick.json) |
| 47 | **FloralWhite** ![FloralWhite](https://github.com/iaseth/html-color-names/blob/master/png/floralwhite.png?raw=true) | `floralwhite` | `#fffaf0` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/floralwhite.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/floralwhite.json) |
| 48 | **ForestGreen** ![ForestGreen](https://github.com/iaseth/html-color-names/blob/master/png/forestgreen.png?raw=true) | `forestgreen` | `#228b22` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/forestgreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/forestgreen.json) |
| 49 | **Fuchsia** ![Fuchsia](https://github.com/iaseth/html-color-names/blob/master/png/fuchsia.png?raw=true) | `fuchsia` | `#ff00ff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/fuchsia.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/fuchsia.json) |
| 50 | **Gainsboro** ![Gainsboro](https://github.com/iaseth/html-color-names/blob/master/png/gainsboro.png?raw=true) | `gainsboro` | `#dcdcdc` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/gainsboro.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/gainsboro.json) |
| 51 | **GhostWhite** ![GhostWhite](https://github.com/iaseth/html-color-names/blob/master/png/ghostwhite.png?raw=true) | `ghostwhite` | `#f8f8ff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/ghostwhite.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/ghostwhite.json) |
| 52 | **Gold** ![Gold](https://github.com/iaseth/html-color-names/blob/master/png/gold.png?raw=true) | `gold` | `#ffd700` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/gold.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/gold.json) |
| 53 | **GoldenRod** ![GoldenRod](https://github.com/iaseth/html-color-names/blob/master/png/goldenrod.png?raw=true) | `goldenrod` | `#daa520` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/goldenrod.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/goldenrod.json) |
| 54 | **Gray** ![Gray](https://github.com/iaseth/html-color-names/blob/master/png/gray.png?raw=true) | `gray` | `#808080` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/gray.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/gray.json) |
| 55 | **Grey** ![Grey](https://github.com/iaseth/html-color-names/blob/master/png/grey.png?raw=true) | `grey` | `#808080` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/grey.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/grey.json) |
| 56 | **Green** ![Green](https://github.com/iaseth/html-color-names/blob/master/png/green.png?raw=true) | `green` | `#008000` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/green.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/green.json) |
| 57 | **GreenYellow** ![GreenYellow](https://github.com/iaseth/html-color-names/blob/master/png/greenyellow.png?raw=true) | `greenyellow` | `#adff2f` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/greenyellow.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/greenyellow.json) |
| 58 | **HoneyDew** ![HoneyDew](https://github.com/iaseth/html-color-names/blob/master/png/honeydew.png?raw=true) | `honeydew` | `#f0fff0` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/honeydew.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/honeydew.json) |
| 59 | **HotPink** ![HotPink](https://github.com/iaseth/html-color-names/blob/master/png/hotpink.png?raw=true) | `hotpink` | `#ff69b4` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/hotpink.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/hotpink.json) |
| 60 | **IndianRed** ![IndianRed](https://github.com/iaseth/html-color-names/blob/master/png/indianred.png?raw=true) | `indianred` | `#cd5c5c` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/indianred.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/indianred.json) |
| 61 | **Indigo** ![Indigo](https://github.com/iaseth/html-color-names/blob/master/png/indigo.png?raw=true) | `indigo` | `#4b0082` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/indigo.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/indigo.json) |
| 62 | **Ivory** ![Ivory](https://github.com/iaseth/html-color-names/blob/master/png/ivory.png?raw=true) | `ivory` | `#fffff0` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/ivory.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/ivory.json) |
| 63 | **Khaki** ![Khaki](https://github.com/iaseth/html-color-names/blob/master/png/khaki.png?raw=true) | `khaki` | `#f0e68c` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/khaki.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/khaki.json) |
| 64 | **Lavender** ![Lavender](https://github.com/iaseth/html-color-names/blob/master/png/lavender.png?raw=true) | `lavender` | `#e6e6fa` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lavender.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lavender.json) |
| 65 | **LavenderBlush** ![LavenderBlush](https://github.com/iaseth/html-color-names/blob/master/png/lavenderblush.png?raw=true) | `lavenderblush` | `#fff0f5` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lavenderblush.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lavenderblush.json) |
| 66 | **LawnGreen** ![LawnGreen](https://github.com/iaseth/html-color-names/blob/master/png/lawngreen.png?raw=true) | `lawngreen` | `#7cfc00` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lawngreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lawngreen.json) |
| 67 | **LemonChiffon** ![LemonChiffon](https://github.com/iaseth/html-color-names/blob/master/png/lemonchiffon.png?raw=true) | `lemonchiffon` | `#fffacd` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lemonchiffon.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lemonchiffon.json) |
| 68 | **LightBlue** ![LightBlue](https://github.com/iaseth/html-color-names/blob/master/png/lightblue.png?raw=true) | `lightblue` | `#add8e6` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightblue.json) |
| 69 | **LightCoral** ![LightCoral](https://github.com/iaseth/html-color-names/blob/master/png/lightcoral.png?raw=true) | `lightcoral` | `#f08080` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightcoral.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightcoral.json) |
| 70 | **LightCyan** ![LightCyan](https://github.com/iaseth/html-color-names/blob/master/png/lightcyan.png?raw=true) | `lightcyan` | `#e0ffff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightcyan.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightcyan.json) |
| 71 | **LightGoldenRodYellow** ![LightGoldenRodYellow](https://github.com/iaseth/html-color-names/blob/master/png/lightgoldenrodyellow.png?raw=true) | `lightgoldenrodyellow` | `#fafad2` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightgoldenrodyellow.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightgoldenrodyellow.json) |
| 72 | **LightGray** ![LightGray](https://github.com/iaseth/html-color-names/blob/master/png/lightgray.png?raw=true) | `lightgray` | `#d3d3d3` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightgray.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightgray.json) |
| 73 | **LightGrey** ![LightGrey](https://github.com/iaseth/html-color-names/blob/master/png/lightgrey.png?raw=true) | `lightgrey` | `#d3d3d3` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightgrey.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightgrey.json) |
| 74 | **LightGreen** ![LightGreen](https://github.com/iaseth/html-color-names/blob/master/png/lightgreen.png?raw=true) | `lightgreen` | `#90ee90` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightgreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightgreen.json) |
| 75 | **LightPink** ![LightPink](https://github.com/iaseth/html-color-names/blob/master/png/lightpink.png?raw=true) | `lightpink` | `#ffb6c1` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightpink.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightpink.json) |
| 76 | **LightSalmon** ![LightSalmon](https://github.com/iaseth/html-color-names/blob/master/png/lightsalmon.png?raw=true) | `lightsalmon` | `#ffa07a` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightsalmon.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightsalmon.json) |
| 77 | **LightSeaGreen** ![LightSeaGreen](https://github.com/iaseth/html-color-names/blob/master/png/lightseagreen.png?raw=true) | `lightseagreen` | `#20b2aa` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightseagreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightseagreen.json) |
| 78 | **LightSkyBlue** ![LightSkyBlue](https://github.com/iaseth/html-color-names/blob/master/png/lightskyblue.png?raw=true) | `lightskyblue` | `#87cefa` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightskyblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightskyblue.json) |
| 79 | **LightSlateGray** ![LightSlateGray](https://github.com/iaseth/html-color-names/blob/master/png/lightslategray.png?raw=true) | `lightslategray` | `#778899` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightslategray.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightslategray.json) |
| 80 | **LightSlateGrey** ![LightSlateGrey](https://github.com/iaseth/html-color-names/blob/master/png/lightslategrey.png?raw=true) | `lightslategrey` | `#778899` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightslategrey.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightslategrey.json) |
| 81 | **LightSteelBlue** ![LightSteelBlue](https://github.com/iaseth/html-color-names/blob/master/png/lightsteelblue.png?raw=true) | `lightsteelblue` | `#b0c4de` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightsteelblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightsteelblue.json) |
| 82 | **LightYellow** ![LightYellow](https://github.com/iaseth/html-color-names/blob/master/png/lightyellow.png?raw=true) | `lightyellow` | `#ffffe0` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lightyellow.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lightyellow.json) |
| 83 | **Lime** ![Lime](https://github.com/iaseth/html-color-names/blob/master/png/lime.png?raw=true) | `lime` | `#00ff00` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/lime.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/lime.json) |
| 84 | **LimeGreen** ![LimeGreen](https://github.com/iaseth/html-color-names/blob/master/png/limegreen.png?raw=true) | `limegreen` | `#32cd32` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/limegreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/limegreen.json) |
| 85 | **Linen** ![Linen](https://github.com/iaseth/html-color-names/blob/master/png/linen.png?raw=true) | `linen` | `#faf0e6` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/linen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/linen.json) |
| 86 | **Magenta** ![Magenta](https://github.com/iaseth/html-color-names/blob/master/png/magenta.png?raw=true) | `magenta` | `#ff00ff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/magenta.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/magenta.json) |
| 87 | **Maroon** ![Maroon](https://github.com/iaseth/html-color-names/blob/master/png/maroon.png?raw=true) | `maroon` | `#800000` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/maroon.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/maroon.json) |
| 88 | **MediumAquaMarine** ![MediumAquaMarine](https://github.com/iaseth/html-color-names/blob/master/png/mediumaquamarine.png?raw=true) | `mediumaquamarine` | `#66cdaa` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumaquamarine.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumaquamarine.json) |
| 89 | **MediumBlue** ![MediumBlue](https://github.com/iaseth/html-color-names/blob/master/png/mediumblue.png?raw=true) | `mediumblue` | `#0000cd` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumblue.json) |
| 90 | **MediumOrchid** ![MediumOrchid](https://github.com/iaseth/html-color-names/blob/master/png/mediumorchid.png?raw=true) | `mediumorchid` | `#ba55d3` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumorchid.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumorchid.json) |
| 91 | **MediumPurple** ![MediumPurple](https://github.com/iaseth/html-color-names/blob/master/png/mediumpurple.png?raw=true) | `mediumpurple` | `#9370db` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumpurple.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumpurple.json) |
| 92 | **MediumSeaGreen** ![MediumSeaGreen](https://github.com/iaseth/html-color-names/blob/master/png/mediumseagreen.png?raw=true) | `mediumseagreen` | `#3cb371` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumseagreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumseagreen.json) |
| 93 | **MediumSlateBlue** ![MediumSlateBlue](https://github.com/iaseth/html-color-names/blob/master/png/mediumslateblue.png?raw=true) | `mediumslateblue` | `#7b68ee` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumslateblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumslateblue.json) |
| 94 | **MediumSpringGreen** ![MediumSpringGreen](https://github.com/iaseth/html-color-names/blob/master/png/mediumspringgreen.png?raw=true) | `mediumspringgreen` | `#00fa9a` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumspringgreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumspringgreen.json) |
| 95 | **MediumTurquoise** ![MediumTurquoise](https://github.com/iaseth/html-color-names/blob/master/png/mediumturquoise.png?raw=true) | `mediumturquoise` | `#48d1cc` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumturquoise.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumturquoise.json) |
| 96 | **MediumVioletRed** ![MediumVioletRed](https://github.com/iaseth/html-color-names/blob/master/png/mediumvioletred.png?raw=true) | `mediumvioletred` | `#c71585` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mediumvioletred.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mediumvioletred.json) |
| 97 | **MidnightBlue** ![MidnightBlue](https://github.com/iaseth/html-color-names/blob/master/png/midnightblue.png?raw=true) | `midnightblue` | `#191970` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/midnightblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/midnightblue.json) |
| 98 | **MintCream** ![MintCream](https://github.com/iaseth/html-color-names/blob/master/png/mintcream.png?raw=true) | `mintcream` | `#f5fffa` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mintcream.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mintcream.json) |
| 99 | **MistyRose** ![MistyRose](https://github.com/iaseth/html-color-names/blob/master/png/mistyrose.png?raw=true) | `mistyrose` | `#ffe4e1` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/mistyrose.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/mistyrose.json) |
| 100 | **Moccasin** ![Moccasin](https://github.com/iaseth/html-color-names/blob/master/png/moccasin.png?raw=true) | `moccasin` | `#ffe4b5` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/moccasin.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/moccasin.json) |
| 101 | **NavajoWhite** ![NavajoWhite](https://github.com/iaseth/html-color-names/blob/master/png/navajowhite.png?raw=true) | `navajowhite` | `#ffdead` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/navajowhite.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/navajowhite.json) |
| 102 | **Navy** ![Navy](https://github.com/iaseth/html-color-names/blob/master/png/navy.png?raw=true) | `navy` | `#000080` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/navy.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/navy.json) |
| 103 | **OldLace** ![OldLace](https://github.com/iaseth/html-color-names/blob/master/png/oldlace.png?raw=true) | `oldlace` | `#fdf5e6` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/oldlace.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/oldlace.json) |
| 104 | **Olive** ![Olive](https://github.com/iaseth/html-color-names/blob/master/png/olive.png?raw=true) | `olive` | `#808000` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/olive.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/olive.json) |
| 105 | **OliveDrab** ![OliveDrab](https://github.com/iaseth/html-color-names/blob/master/png/olivedrab.png?raw=true) | `olivedrab` | `#6b8e23` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/olivedrab.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/olivedrab.json) |
| 106 | **Orange** ![Orange](https://github.com/iaseth/html-color-names/blob/master/png/orange.png?raw=true) | `orange` | `#ffa500` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/orange.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/orange.json) |
| 107 | **OrangeRed** ![OrangeRed](https://github.com/iaseth/html-color-names/blob/master/png/orangered.png?raw=true) | `orangered` | `#ff4500` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/orangered.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/orangered.json) |
| 108 | **Orchid** ![Orchid](https://github.com/iaseth/html-color-names/blob/master/png/orchid.png?raw=true) | `orchid` | `#da70d6` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/orchid.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/orchid.json) |
| 109 | **PaleGoldenRod** ![PaleGoldenRod](https://github.com/iaseth/html-color-names/blob/master/png/palegoldenrod.png?raw=true) | `palegoldenrod` | `#eee8aa` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/palegoldenrod.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/palegoldenrod.json) |
| 110 | **PaleGreen** ![PaleGreen](https://github.com/iaseth/html-color-names/blob/master/png/palegreen.png?raw=true) | `palegreen` | `#98fb98` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/palegreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/palegreen.json) |
| 111 | **PaleTurquoise** ![PaleTurquoise](https://github.com/iaseth/html-color-names/blob/master/png/paleturquoise.png?raw=true) | `paleturquoise` | `#afeeee` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/paleturquoise.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/paleturquoise.json) |
| 112 | **PaleVioletRed** ![PaleVioletRed](https://github.com/iaseth/html-color-names/blob/master/png/palevioletred.png?raw=true) | `palevioletred` | `#db7093` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/palevioletred.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/palevioletred.json) |
| 113 | **PapayaWhip** ![PapayaWhip](https://github.com/iaseth/html-color-names/blob/master/png/papayawhip.png?raw=true) | `papayawhip` | `#ffefd5` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/papayawhip.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/papayawhip.json) |
| 114 | **PeachPuff** ![PeachPuff](https://github.com/iaseth/html-color-names/blob/master/png/peachpuff.png?raw=true) | `peachpuff` | `#ffdab9` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/peachpuff.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/peachpuff.json) |
| 115 | **Peru** ![Peru](https://github.com/iaseth/html-color-names/blob/master/png/peru.png?raw=true) | `peru` | `#cd853f` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/peru.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/peru.json) |
| 116 | **Pink** ![Pink](https://github.com/iaseth/html-color-names/blob/master/png/pink.png?raw=true) | `pink` | `#ffc0cb` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/pink.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/pink.json) |
| 117 | **Plum** ![Plum](https://github.com/iaseth/html-color-names/blob/master/png/plum.png?raw=true) | `plum` | `#dda0dd` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/plum.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/plum.json) |
| 118 | **PowderBlue** ![PowderBlue](https://github.com/iaseth/html-color-names/blob/master/png/powderblue.png?raw=true) | `powderblue` | `#b0e0e6` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/powderblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/powderblue.json) |
| 119 | **Purple** ![Purple](https://github.com/iaseth/html-color-names/blob/master/png/purple.png?raw=true) | `purple` | `#800080` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/purple.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/purple.json) |
| 120 | **RebeccaPurple** ![RebeccaPurple](https://github.com/iaseth/html-color-names/blob/master/png/rebeccapurple.png?raw=true) | `rebeccapurple` | `#663399` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/rebeccapurple.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/rebeccapurple.json) |
| 121 | **Red** ![Red](https://github.com/iaseth/html-color-names/blob/master/png/red.png?raw=true) | `red` | `#ff0000` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/red.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/red.json) |
| 122 | **RosyBrown** ![RosyBrown](https://github.com/iaseth/html-color-names/blob/master/png/rosybrown.png?raw=true) | `rosybrown` | `#bc8f8f` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/rosybrown.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/rosybrown.json) |
| 123 | **RoyalBlue** ![RoyalBlue](https://github.com/iaseth/html-color-names/blob/master/png/royalblue.png?raw=true) | `royalblue` | `#4169e1` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/royalblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/royalblue.json) |
| 124 | **SaddleBrown** ![SaddleBrown](https://github.com/iaseth/html-color-names/blob/master/png/saddlebrown.png?raw=true) | `saddlebrown` | `#8b4513` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/saddlebrown.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/saddlebrown.json) |
| 125 | **Salmon** ![Salmon](https://github.com/iaseth/html-color-names/blob/master/png/salmon.png?raw=true) | `salmon` | `#fa8072` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/salmon.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/salmon.json) |
| 126 | **SandyBrown** ![SandyBrown](https://github.com/iaseth/html-color-names/blob/master/png/sandybrown.png?raw=true) | `sandybrown` | `#f4a460` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/sandybrown.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/sandybrown.json) |
| 127 | **SeaGreen** ![SeaGreen](https://github.com/iaseth/html-color-names/blob/master/png/seagreen.png?raw=true) | `seagreen` | `#2e8b57` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/seagreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/seagreen.json) |
| 128 | **SeaShell** ![SeaShell](https://github.com/iaseth/html-color-names/blob/master/png/seashell.png?raw=true) | `seashell` | `#fff5ee` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/seashell.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/seashell.json) |
| 129 | **Sienna** ![Sienna](https://github.com/iaseth/html-color-names/blob/master/png/sienna.png?raw=true) | `sienna` | `#a0522d` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/sienna.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/sienna.json) |
| 130 | **Silver** ![Silver](https://github.com/iaseth/html-color-names/blob/master/png/silver.png?raw=true) | `silver` | `#c0c0c0` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/silver.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/silver.json) |
| 131 | **SkyBlue** ![SkyBlue](https://github.com/iaseth/html-color-names/blob/master/png/skyblue.png?raw=true) | `skyblue` | `#87ceeb` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/skyblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/skyblue.json) |
| 132 | **SlateBlue** ![SlateBlue](https://github.com/iaseth/html-color-names/blob/master/png/slateblue.png?raw=true) | `slateblue` | `#6a5acd` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/slateblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/slateblue.json) |
| 133 | **SlateGray** ![SlateGray](https://github.com/iaseth/html-color-names/blob/master/png/slategray.png?raw=true) | `slategray` | `#708090` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/slategray.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/slategray.json) |
| 134 | **SlateGrey** ![SlateGrey](https://github.com/iaseth/html-color-names/blob/master/png/slategrey.png?raw=true) | `slategrey` | `#708090` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/slategrey.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/slategrey.json) |
| 135 | **Snow** ![Snow](https://github.com/iaseth/html-color-names/blob/master/png/snow.png?raw=true) | `snow` | `#fffafa` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/snow.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/snow.json) |
| 136 | **SpringGreen** ![SpringGreen](https://github.com/iaseth/html-color-names/blob/master/png/springgreen.png?raw=true) | `springgreen` | `#00ff7f` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/springgreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/springgreen.json) |
| 137 | **SteelBlue** ![SteelBlue](https://github.com/iaseth/html-color-names/blob/master/png/steelblue.png?raw=true) | `steelblue` | `#4682b4` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/steelblue.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/steelblue.json) |
| 138 | **Tan** ![Tan](https://github.com/iaseth/html-color-names/blob/master/png/tan.png?raw=true) | `tan` | `#d2b48c` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/tan.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/tan.json) |
| 139 | **Teal** ![Teal](https://github.com/iaseth/html-color-names/blob/master/png/teal.png?raw=true) | `teal` | `#008080` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/teal.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/teal.json) |
| 140 | **Thistle** ![Thistle](https://github.com/iaseth/html-color-names/blob/master/png/thistle.png?raw=true) | `thistle` | `#d8bfd8` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/thistle.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/thistle.json) |
| 141 | **Tomato** ![Tomato](https://github.com/iaseth/html-color-names/blob/master/png/tomato.png?raw=true) | `tomato` | `#ff6347` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/tomato.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/tomato.json) |
| 142 | **Turquoise** ![Turquoise](https://github.com/iaseth/html-color-names/blob/master/png/turquoise.png?raw=true) | `turquoise` | `#40e0d0` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/turquoise.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/turquoise.json) |
| 143 | **Violet** ![Violet](https://github.com/iaseth/html-color-names/blob/master/png/violet.png?raw=true) | `violet` | `#ee82ee` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/violet.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/violet.json) |
| 144 | **Wheat** ![Wheat](https://github.com/iaseth/html-color-names/blob/master/png/wheat.png?raw=true) | `wheat` | `#f5deb3` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/wheat.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/wheat.json) |
| 145 | **White** ![White](https://github.com/iaseth/html-color-names/blob/master/png/white.png?raw=true) | `white` | `#ffffff` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/white.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/white.json) |
| 146 | **WhiteSmoke** ![WhiteSmoke](https://github.com/iaseth/html-color-names/blob/master/png/whitesmoke.png?raw=true) | `whitesmoke` | `#f5f5f5` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/whitesmoke.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/whitesmoke.json) |
| 147 | **Yellow** ![Yellow](https://github.com/iaseth/html-color-names/blob/master/png/yellow.png?raw=true) | `yellow` | `#ffff00` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/yellow.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/yellow.json) |
| 148 | **YellowGreen** ![YellowGreen](https://github.com/iaseth/html-color-names/blob/master/png/yellowgreen.png?raw=true) | `yellowgreen` | `#9acd32` | [CSS](https://github.com/iaseth/html-color-names/blob/master/css/yellowgreen.css) | [JSON](https://github.com/iaseth/html-color-names/blob/master/json/yellowgreen.json) |

